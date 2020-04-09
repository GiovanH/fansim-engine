from PIL import Image
from PIL import ImageChops
import os
import re
import glob
import math
import _logging

logger = _logging.getLogger(__name__)


SEP = "_"
REPLACE_THRESHHOLD = 0.5  # How much more efficient the patch needs to be than just using the image outright.


def distance(t1, t2):
    """Returns the distance between two points in n-dimensional space.
    Used for determining the difference between two RGBA colors.
    Coordinate length must match.

    Args:
        t1 (tuple): Coordinates
        t2 (tuple): Coordinates

    Returns:
        float: Distance
    """
    e2 = 0
    for a, b in zip(t1, t2):
        e2 += (a - b) ** 2
    return math.sqrt(e2)


def getWhere(list, matches, default=None):
    for item in list:
        if matches(item):
            return item
    return default


def ensurePath(filepath):
    dir_part, filename = os.path.split(filepath)
    if not os.path.isdir(dir_part):
        os.makedirs(dir_part, exist_ok=True)


class Pose():

    def __init__(self, char_name, expression_t):
        super(Pose, self).__init__()
        self.char_name = char_name
        self.expression_t = expression_t
        self.dirty = False
        self.image = None
        self.imver = 0
        self.parent = None
        self.children = []

    def loadImage(self, image_path):
        self.source_path = image_path
        return self.setImage(Image.open(image_path).convert('RGBA'))

    def getImage(self):
        return self.image.copy()

    def setImage(self, new_image):
        self.dirty = True
        self.image = new_image
        self.imver += 1
        # self.saveImageDebug()
        return self

    def saveImageDebug(self):
        ensurePath(self.out_filepath_real)
        self.image.save(self.out_filepath_real + f".WORKING.v{self.imver}.png")
        # logger.info(f"Saved {self} v{self.imver}")

    def saveImage(self):
        ensurePath(self.out_filepath_real)
        self.image.save(self.out_filepath_real)
        self.dirty = False

    @property
    def out_filepath_real(self):
        return self.out_filepath_logical.replace("{{assets}}", "rpydiff_out")

    @property
    def out_filename(self):
        return SEP.join(self.expression_t) + ".png"

    @property
    def out_filepath_logical(self):
        return "{{assets}}" + f"/characterp/{self.char_name}/{self.out_filename}"

    @property
    def rpy_qualified_name(self):
        return f"!{self.char_name} {' '.join(self.expression_t)}"

    @property
    def rpy_definition(self):
        if self.dirty:
            logger.warning(f"Generated rpy_definition for '{self.rpy_qualified_name}' while dirty!")
        return f'image {self.rpy_qualified_name} = "{self.out_filepath_logical}"\n'

    def __repr__(self):
        return f"<{type(self).__name__} {self.char_name} {' '.join(self.expression_t)} v{self.imver}{'*' if self.dirty else ''}>"


def poseFromFile(posefilepath):
    a, b = os.path.split(posefilepath)
    char_name = os.path.split(a)[1]
    file_plainname, file_ext = os.path.splitext(b)
    subposes = re.split(r"[ _-]", file_plainname)
    return Pose(char_name, subposes).loadImage(posefilepath)


class PatchPose(Pose):
    def __init__(self, parent_pose, child_pose, new_image, x1, y1):
        super().__init__(child_pose.char_name, child_pose.expression_t)
        self.x = x1
        self.y = y1
        self.parent = parent_pose
        self.parent_size = self.parent.getImage().size
        self.full = child_pose
        self.setImage(new_image)

    def patchIsEfficient(self):
        import operator
        patch_size = operator.mul(*self.getImage().size)
        replace_size = operator.mul(*self.full.getImage().size)
        # logger.info(f"{self} {patch_size} {replace_size} {(patch_size/replace_size)=}")
        return (patch_size / replace_size) < REPLACE_THRESHHOLD

    def validate(self):
        assert self.parent_size == self.parent.getImage().size

    @property
    def out_filename(self):
        return SEP.join(self.expression_t) + f" {self.x},{self.y}.png"

    @property
    def rpy_definition(self):
        self.validate()
        if self.dirty:
            logger.warning(f"Generated rpy_definition for '{self.rpy_qualified_name}' while dirty!")
        return f"""image {self.rpy_qualified_name} = Composite(
    {self.parent_size},
    (0, 0), "{self.parent.rpy_qualified_name.replace('!', '__p__')}",
    ({self.x}, {self.y}), "{self.out_filepath_logical}"
)\n"""

    def __repr__(self):
        return f"<{type(self).__name__} {self.char_name} {' '.join(self.expression_t)} v{self.imver}{'*' if self.dirty else ''} @{self.x},{self.y}>"


class LogicalPose(Pose):

    def saveImage(self):
        return

    def withOutFilename(self, out_filename):
        self._out_filename = out_filename
        return self

    @property
    def out_filename(self):
        return self._out_filename


def expandCanvasToFit(parent_pose, subpose):
    # Ensures that original_pose is at least as big as update_pose
    old_parent_image = parent_pose.getImage()
    subpose_image = subpose.getImage()
    bigger_size = (*[max(a, b) for a, b in zip(old_parent_image.size, subpose_image.size)],)
    if bigger_size != old_parent_image.size:
        logger.debug(f"Resizing {parent_pose} from {old_parent_image.size} up to {bigger_size} to fit {subpose}")

        new_parent_image = Image.new("RGBA", bigger_size, color=(0, 0, 0, 0))
        x1 = (bigger_size[0] - old_parent_image.size[0]) // 2
        y1 = bigger_size[1] - old_parent_image.size[1]
        # print("pasting at", (x1, y1))
        new_parent_image.paste(old_parent_image, (x1, y1))
        parent_pose.setImage(new_parent_image)
    return


def spriteTrim(pose):
    sprite_image = pose.getImage()

    # sprite_nonmask = sprite_image.transpose(Image.FLIP_LEFT_RIGHT)
    # sprite_nonmask.paste(sprite_image, (0, 0), sprite_image)

    bbox_orig = (0, 0, *sprite_image.size)
    bbox_cropped = sprite_image.getbbox()

    if bbox_orig == bbox_cropped:
        # Clean transparency
        pixdata = sprite_image.load()
        # if pixdata[0, 0] != (0, 0, 0, 0):
        for y in range(sprite_image.size[1]):
            for x in range(sprite_image.size[0]):
                if pixdata[x, y][3] == 0:
                    pixdata[x, y] = (0, 0, 0, 0)
        bbox_cropped = sprite_image.getbbox()
        if bbox_orig == bbox_cropped:
            logger.debug(f"{pose} already cropped at {bbox_orig}")
            return

    side_space = min((bbox_cropped[0] - bbox_orig[0]), (bbox_orig[2] - bbox_cropped[2]))
    # assert (bbox_cropped[0] - bbox_orig[0]) == (bbox_orig[2] - bbox_cropped[2])

    bbox_cropped = (
        bbox_orig[0] + side_space,
        bbox_orig[1],
        bbox_orig[2] - side_space,
        bbox_orig[3]
    )

    # if bbox_orig == bbox_mirrored:
    #     return

    # bigger_size = (*[max(a, b) for a, b in zip(old_parent_image.size, subpose_image.size)],)

    logger.debug(f"Cropping {pose} from {bbox_orig} to {bbox_cropped}")
    pose.setImage(sprite_image.crop(bbox_cropped))


def getPatch(original_pose, update_pose, fuzz=255, box_pad=20):
    logger.info(f"Creating patch for {original_pose} from {update_pose}")
    expandCanvasToFit(update_pose, original_pose)

    original = original_pose.getImage()
    update = update_pose.getImage()

    w, h = original.size
    originalp = original.load()
    updatep = update.load()

    x1, y1 = w, h
    x2 = 0
    y2 = 0

    for x in range(w):    # for every col:
        for y in range(h):    # For every row
            op = originalp[x, y]
            up = updatep[x, y]
            same = (op == up) or (op[3] == 0 and up[3] == 0)
            if not same and distance(op, up) > fuzz:
                x1 = min(x1, x)
                y1 = min(y1, y)
                x2 = max(x2, x + 1)
                y2 = max(y2, y + 1)
                if op[3] == 255 and up[3] == 0:
                    # If we're trying to "add transparency", that won't work; fail
                    logger.warning(f"Invalid transparency manipulation: {op[3]=} > {up[3]=} at {(x, y)=}")
                    return update_pose

    x1 = max(x1 - box_pad, 0)
    y1 = max(y1 - box_pad, 0)
    x2 = min(x2 + box_pad, w)
    y2 = min(y2 + box_pad, h)

    logger.debug(f"Leaving patch {update_pose} at {(x1, y1, x2, y2,)}")
    diff = update.crop((x1, y1, x2, y2,))

    bbox = diff.getbbox()
    if not bbox:
        return LogicalPose(update_pose.char_name, update_pose.expression_t).withOutFilename(original_pose.out_filename)

    # print(diff.size, original.size, bbox != original.size)
    new_patch = PatchPose(original_pose, update_pose, diff, x1, y1)
    if new_patch.patchIsEfficient():
        return new_patch
    else:
        logger.warning("Patch is inefficient, not using.")
        return update_pose


def processPoses(all_poses, trim, patch, rpy_outpath):
    if trim:
        logger.info("Trimming pose sprites...")
        for pose in all_poses:
            spriteTrim(pose)

    logger.info("Building pose hierarchy...")

    global_parent = None
    for name in ["neutral", "idle", "normal", "standing", "smile", "grin", "happy"]:
        c = getWhere(all_poses, lambda p: p.expression_t == [name])
        if c:
            global_parent = c
            break
    logger.info(f"Global parent {global_parent}")

    for pose in sorted(all_poses, key=lambda p: -len(p.expression_t)):
        # while True:
        target_parent_et = pose.expression_t[:-1]
        pose.parent = getWhere(all_poses, lambda p: p.expression_t == target_parent_et)
        if not pose.parent and pose != global_parent:
            pose.parent = global_parent
        if pose.parent:
            pose.parent.children.append(pose)

    if patch:
        logger.info("Generating patches...")
        for parent in sorted(all_poses, key=lambda p: len(p.expression_t)):
            # logger.info(f"Parent {parent}")
            for subpose in parent.children:
                expandCanvasToFit(parent, subpose)
            for subpose in parent.children:
                # logger.info(f"Child {subpose}")
                new_patch = getPatch(parent, subpose)
                if new_patch:
                    all_poses.remove(subpose)
                    all_poses.append(new_patch)

    with open(rpy_outpath, "w") as rpyfp:
        for pose in sorted(all_poses, key=lambda p: len(p.expression_t)):
            pose.saveImage()
            rpyfp.write(pose.rpy_definition)


def main():
    import argparse
    ap = argparse.ArgumentParser()

    def add_bool_arg(parser, name, default=True, help=None):
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument('--' + name, dest=name, action='store_true', help=help + f" (Default: {default})")
        group.add_argument('--no-' + name, dest=name, action='store_false', help=help + f" (Default: {default})")
        parser.set_defaults(**{name: default})
    # ap.add_argument(
    #     '--character-yaml', nargs="+", default=[],
    #     help="Character definitions, in yaml format"
    # )
    ap.add_argument(
        '--character-dirs', nargs="+", default=[],
        help="Character definitions, in raw directories"
    )
    ap.add_argument(
        "--rpy-out", default=None,
        help="Output rpy filename")

    add_bool_arg(ap, "trim", default=True, help="Remove whitespace from around sprites")
    add_bool_arg(ap, "patch", default=True, help="Generate patches to compress character sprites")

    args = ap.parse_args()

    for sprite_dir in args.character_dirs:
        all_poses = []
        logger.info("Loading poses from file...")
        for pngfile in glob.glob(os.path.join(sprite_dir, "*.png")):
            all_poses.append(poseFromFile(pngfile))

        sprite_name_auto = os.path.split(os.path.split(os.path.join(sprite_dir, ""))[0])[1]  # sorry
        rpy_outpath = os.path.join("rpydiff_out", args.rpy_out or sprite_name_auto + ".rpy")
        processPoses(all_poses, args.trim, args.patch, rpy_outpath)


if __name__ == "__main__":
    main()
