from PIL import Image
from PIL import ImageChops
import os
import re
import glob
import math
import _logging
import yaml
import threading
import shutil

logger = _logging.getLogger(__name__)

SEP = "_"
REPLACE_THRESHHOLD = 0.5 # 0.5  # How much more efficient the patch needs to be than just using the image outright.


use_threading = False
LAZY_THREADS = []
PREFIXED_WITH_NAME = True
EXTRA_IM_PARAMS = ", yanchor=0.95"

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


def makePatchDemo(new_patch, rev=""):
    out_path_demo = new_patch.out_filepath_real.replace("rpydiff_out", "rpydiff_out_demo")    
    ensurePath(out_path_demo)

    original_image = new_patch.parent.getImage()
    original_image_p = Image.new("RGBA", original_image.size, color=(255, 0, 255, 255,))
    original_image_p.paste(original_image, mask=original_image)
    # original_image_p.save(out_path_demo + ".diff.png")

    update_image = new_patch.getImage()
    update_image_p = Image.new("RGBA", update_image.size, color=(0, 0, 0, 255))
    update_image_p.paste(update_image, mask=update_image)
    ImageChops.difference(
        original_image_p.convert("RGB"), 
        update_image.convert("RGB")
    ).save(out_path_demo + f".diff{rev}.png")


def expandImageToFit(old_container, target_size):
    bigger_size = (*[max(a, b) for a, b in zip(old_container.size, target_size)],)
    if bigger_size != old_container.size:
        
        new_container = Image.new("RGBA", bigger_size, color=(0, 0, 0, 0))
        x1 = (bigger_size[0] - old_container.size[0]) // 2
        y1 = bigger_size[1] - old_container.size[1]
        # print("pasting at", (x1, y1))
        new_container.paste(old_container, (x1, y1))
        return new_container
    return old_container


class Pose():
    api = {
        "source": "source_path",
        "pose": "expression_t",
        "rpy_override": "_rpy_qualified_name"
    }

    def __init__(self, char_name, expression_t):
        super(Pose, self).__init__()
        self.char_name = char_name
        self.expression_t = [w.lower() for w in expression_t]
        self.dirty = False
        self.image = None
        self.imver = 0
        self.parent = None
        self.children = []
        self._rpy_qualified_name = None

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
        out_filepath_debug = self.out_filepath_real + f".WORKING.v{self.imver}.png"
        ensurePath(out_filepath_debug)
        self.image.save(out_filepath_debug)
        # logger.info(f"Saved {self} v{self.imver}")

    def saveImage(self):
        ensurePath(self.out_filepath_real)
        self.image.save(self.out_filepath_real)
        self.dirty = False

    def expandToFit(self, subpose):
        old_container = self.getImage()
        new_image = expandImageToFit(old_container, subpose.getImage().size)
        if new_image != old_container:
            logger.info(f"Resizing {self} from {old_container.size} up to {new_image.size} to fit {subpose}")
            self.setImage(new_image)
        return

    def onParentShift(self, dx, dy):
        for pose in self.children:
            pose.onParentShift(dx, dy)

    def spriteTrim(self):
        sprite_image = self.getImage()

        cropped, dx, dy = imageTrim(sprite_image)
        if cropped != sprite_image:
            logger.info(f"Cropping {self} from {sprite_image.getbbox()} to {cropped.getbbox()}")
            self.setImage(cropped)
            for pose in self.children:
                pose.onParentShift(-dx, dy)
        else:
            logger.debug(f"{self} already cropped at {sprite_image.getbbox()}")

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
        return self._rpy_qualified_name or f"!{self.char_name} {' '.join(self.expression_t)}"

    @property
    def rpy_definition(self):
        if self.dirty:
            logger.warning(f"Generated rpy_definition for '{self.rpy_qualified_name}' while dirty!")
        return f'image {self.rpy_qualified_name} = Image("{self.out_filepath_logical}"{EXTRA_IM_PARAMS})\n'

    def __repr__(self):
        return f"<{type(self).__name__} {self.char_name} {' '.join(self.expression_t)} v{self.imver}{'*' if self.dirty else ''} of {self.parent.rpy_qualified_name if self.parent else None}>"


class PatchPose(Pose):
    def __init__(self, parent_pose, child_pose, new_image, x1, y1):
        super().__init__(child_pose.char_name, child_pose.expression_t)
        self.x = x1
        self.y = y1
        self.parent = parent_pose
        self.parent_size = self.parent.getImage().size
        self.full = child_pose
        self.children = child_pose.children
        self.setImage(new_image)

    def patchIsEfficient(self):
        import operator
        patch_size = operator.mul(*self.image.size)
        replace_size = operator.mul(*self.full.getImage().size)
        # logger.info(f"{self} {patch_size} {replace_size} {(patch_size/replace_size)=}")
        is_efficient = (patch_size / replace_size) < REPLACE_THRESHHOLD
        logger.debug(f"Patch is {'' if is_efficient else 'in'}efficient {patch_size}/{replace_size} = {(patch_size / replace_size)} <? {REPLACE_THRESHHOLD}")
        return is_efficient

    def validate(self):
        if (self.parent_size != self.parent.getImage().size):
            logger.error(f"{self} parent {self.parent} had size changed! {self.parent_size=} != {self.parent.getImage().size=}")

    def expandToFit(self, subpose):
        raise NotImplementedError

    def spriteTrim(self):
        return

    def onParentShift(self, dx, dy):
        logger.debug(f"{self} parent cropped! {dx=}, {dy=}")
        if isinstance(self.parent, PatchPose):
            return
        ddx, ddy = 0, 0
        logger.debug(f"{ddx=} += {dx=}")
        logger.debug(f"{ddy=} += {dy=}")
        ddx += dx
        ddy += dy

        # if isinstance(self.parent, PatchPose):
        #     logger.debug(f"{ddx=} -= {self.parent.x=}")
        #     logger.debug(f"{ddy=} -= {self.parent.y=}")
        #     ddy -= self.parent.y
        #     ddx -= self.parent.x
        # I'm sure this makes sense. I'm not sure why it does.
        # Your position is relative to the parent. But isn't it already?

        self.parent_size = self.parent.getImage().size
        self.x += ddx
        self.y += ddy
        logger.debug(f"{self.x=} += {ddx=}")
        logger.debug(f"{self.y=} += {ddy=}")
        logger.debug(f"Now {self}")

        # We weren't actually cropped! Children don't care
        for pose in self.children:
            pose.onParentShift(ddx, ddy)

    def getImage(self):
        # Emulate ren'py sprite composition
        # I'm sure this bit with max() makes sense. I'm not sure why it does.
        parent_image = self.parent.getImage()
        # i = expandImageToFit(parent_image, self.image.size)



        # margins = tuple(map(lambda i, j: i - j, parent_image.size, i.size))

        # place_at = (self.x, self.y)  # (max(self.x, 0), max(self.y, 0))
        # logger.debug(f"GetImage {self=} {parent_image.size=} {margins=} {self.image.size=} {i.size=} {place_at=}")
        # i.paste(self.image, place_at)  # Don't mask: rpy doesn't
        # return i


        pw, ph = parent_image.size 
        px, py = 0, 0

        sw, sh = self.image.size

        canvas_x1 = min(self.x, px)
        canvas_x2 = max(self.x + sw, px + pw)
        canvas_y1 = min(self.y, py)
        canvas_y2 = max(self.y + sh, py + ph)

        canvas_width = canvas_x2 - canvas_x1
        canvas_height = canvas_y2 - canvas_y1

        spx = self.x - canvas_x1
        spy = self.y - canvas_y1

        ppx = px - canvas_x1
        ppy = py - canvas_y1

        canvas = Image.new("RGBA", (canvas_width, canvas_height), color=(255, 0, 255, 255))

        canvas.paste(parent_image, (ppx, ppy))
        canvas.paste(self.image, (spx, spy))

        return canvas

    def setImage(self, *args):
        if self.image:
            raise NotImplementedError()
        else:
            super().setImage(*args)

    @property
    def out_filename(self):
        return SEP.join(self.expression_t) + f" {self.x},{self.y}.png"

    @property
    def rpy_definition(self):
        self.validate()
        if self.dirty:
            logger.warning(f"Generated rpy_definition for '{self.rpy_qualified_name}' while dirty!")

        pw, ph = self.parent_size
        sw, sh = self.image.size
        rpy_parent_ref = f"\"{self.parent.rpy_qualified_name.replace('!', '__p__')}\""
        rpy_self_ref = f"\"{self.out_filepath_logical}\""

        top = f"(0, 0), Crop((0, 0, {pw}, {self.y}), {rpy_parent_ref})"
        left = f"(0, {self.y}), Crop((0, {self.y}, {self.x}, {self.y + sh}), {rpy_parent_ref})"
        center = f"({self.x}, {self.y}), Image({rpy_self_ref})"
        right = f"({self.x + sw}, {self.y}), Crop(({self.x + sw}, {self.y}, {pw}, {self.y + sh}), {rpy_parent_ref})"
        bottom = f"(0, {self.y + sh}), Crop((0, {self.y + sh}, {pw}, {ph}), {rpy_parent_ref})"

        return f"""image {self.rpy_qualified_name} = Composite(
    {self.parent_size},
    {top},
    {left},
    {center},
    {right},
    {bottom}{EXTRA_IM_PARAMS}
)\n"""

# """
#     {top},
#     {left},
#     {center},
#     {right},
#     {bottom}
# """

    def __repr__(self):
        return f"<{type(self).__name__} {self.char_name} {' '.join(self.expression_t)} v{self.imver}{'*' if self.dirty else ''} of {self.parent.rpy_qualified_name}@{self.x},{self.y}>"


class LogicalPose(Pose):

    def saveImage(self):
        return

    def withOutFilename(self, out_filename):
        self._out_filename = out_filename
        return self

    @property
    def out_filename(self):
        return self._out_filename


def imageTrim(sprite_image):
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
            return (sprite_image, 0, 0)

    side_space = min((bbox_cropped[0] - bbox_orig[0]), (bbox_orig[2] - bbox_cropped[2]))
    # assert (bbox_cropped[0] - bbox_orig[0]) == (bbox_orig[2] - bbox_cropped[2])

    top_crop = bbox_orig[1] - bbox_cropped[1]

    bbox_cropped = (
        bbox_orig[0] + side_space,
        bbox_orig[1] - top_crop,
        bbox_orig[2] - side_space,
        bbox_orig[3]
    )

    return (sprite_image.crop(bbox_cropped), side_space, top_crop)


def getPatch(update_pose, box_pad=20, make_demo=False):
    logger.info(f"Creating patch of {update_pose}")
    original_pose = update_pose.parent
    update_pose.expandToFit(original_pose)

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
                # if op[3] == 255 and up[3] == 0:
                #     # If we're trying to "add transparency", that won't work; fail
                #     logger.warning(f"Invalid transparency manipulation: {op[3]=} > {up[3]=} at {(x, y)=}")
                #     ImageChops.difference(original, update).save(f"debug {update_pose.out_filename}")
                #     return update_pose

    x1 = max(x1 - box_pad, 0)
    y1 = max(y1 - box_pad, 0)
    x2 = min(x2 + box_pad, w)
    y2 = min(y2 + box_pad, h)

    logger.debug(f"Leaving patch {update_pose} at {(x1, y1, x2, y2,)}")
    diff = update.crop((x1, y1, x2, y2,))

    bbox = diff.getbbox()
    if not bbox:
        logger.warn(f"No difference between {update_pose} and {update_pose.parent}")
        return LogicalPose(update_pose.char_name, update_pose.expression_t).withOutFilename(original_pose.out_filename)

    # print(diff.size, original.size, bbox != original.size)
    new_patch = PatchPose(original_pose, update_pose, diff, x1, y1)

    if make_demo:
        if use_threading:
            new_thread = threading.Thread(target=makePatchDemo, args=(new_patch,))
            LAZY_THREADS.append(new_thread)
            new_thread.start()
        else:
            makePatchDemo(new_patch)

    if new_patch.patchIsEfficient():
        return new_patch
    else:
        # new_patch.setImage(ImageChops.difference(original, update))
        return None  # update_pose


def processPoses(all_poses, trim, patch, rpy_outpath, make_demo=False):
    logger.info("Building pose hierarchy...")

    global_parent = None
    for name in ["neutral", "idle", "normal", "standing", "smile", "grin", "happy"]:
        c = getWhere(all_poses, lambda p: p.expression_t == [name])
        if c:
            global_parent = c
            break
    if not global_parent:
        global_parent = all_poses[0]
    logger.info(f"Global parent {global_parent}")

    for pose in sorted(all_poses, key=lambda p: -len(p.expression_t)):
        # while True:
        if pose != global_parent:
            # Try to get an exact match for the expression substring
            target_parent_et = pose.expression_t[:-1]
            pose.parent = getWhere(all_poses, lambda p: p.expression_t == target_parent_et)
            if not pose.parent:
                # Get a partial match, i.e. set a sibling to a parent
                # Not working: must check for recursive loops somehow
                # pose.parent = getWhere(all_poses, lambda p: p.expression_t[:len(target_parent_et)] == target_parent_et and p != pose)

                # This doesn't work. Breaks everything. Not sure why.
                # for name in ["neutral", "idle", "normal", "standing", "smile", "grin", "happy"][::-1]:
                #     target_parent_et_2 = (target_parent_et + [name])
                #     # logger.debug(f"target {target_parent_et_2=} from {target_parent_et} {pose}")
                #     if not pose.parent:
                #         for p in all_poses:
                #             if p != pose and p != global_parent:
                #                 # logger.debug(f"et {p.expression_t=}")
                #                 if p.expression_t == target_parent_et_2:
                #                     pose.parent = p
                if not pose.parent:
                    # Fallback: use global parent
                    pose.parent = global_parent
            if pose.parent:
                logger.debug(f"{pose} assigned parent {pose.parent}")
                pose.parent.children.append(pose)

    def getAllPosesFromTree(root=global_parent):
        for subpose in root.children:
            for p in getAllPosesFromTree(subpose):
                yield p
        yield root

    def printAllPosesFromTree(root=global_parent, level=0):
        logger.info(level * "  " + f" - {root}")
        for subpose in root.children:
            printAllPosesFromTree(subpose, level=level + 1)
    printAllPosesFromTree()

    assert len(list(getAllPosesFromTree())) == len(all_poses)

    if patch:
        def makePatchesFromParent(parent_pose):
            for subpose in parent_pose.children:
                makePatchesFromParent(subpose)
            logger.debug(f"Making patches from parent pose {parent_pose} with children {parent_pose.children}")
            for subpose in list(parent_pose.children):  # Quick copy, so we can add children
                assert subpose.parent is parent_pose
                new_patch = getPatch(subpose, make_demo=make_demo)
                if new_patch:
                    logger.debug(f"{subpose} becomes {new_patch}")
                    for subchild in subpose.children:
                        subchild.parent = new_patch
                    parent_pose.children.remove(subpose)
                    parent_pose.children.append(new_patch)
                # Do not loose children!
                try:
                    assert len(list(getAllPosesFromTree())) == len(all_poses)
                except AssertionError:
                    printAllPosesFromTree()
                    raise

        logger.info("Expanding canvases...")

        max_height = max(p.image.size[1] for p in getAllPosesFromTree())
        max_width = max(p.image.size[0] for p in getAllPosesFromTree())
        max_size_canvas = Pose("canvas", []).setImage(Image.new("1", (max_width, max_height)))
        for pose in getAllPosesFromTree():
            pose.expandToFit(max_size_canvas)
        # This is a way to get around dynamically resizing PatchPoses. Sorry.
        # done = False
        # last_size_sets = set()
        # while True:
        #     this_size_sets = set(p.image.size for p in getAllPosesFromTree())
        #     if len(this_size_sets) == len(last_size_sets):
        #         break
        #     last_size_sets = this_size_sets

        #     for parent_pose in getAllPosesFromTree():
        #         for subpose in getAllPosesFromTree(parent_pose):
        #             subpose.expandToFit(parent_pose)
        #             parent_pose.expandToFit(subpose)

        logger.info("Generating patches...")

        makePatchesFromParent(global_parent)
        # globals().update(locals())

    printAllPosesFromTree()

    if trim:
        logger.info("Trimming pose sprites...")
        for pose in getAllPosesFromTree():
            logger.info(f"Trimming {pose} sprites...")
            pose.spriteTrim()

        printAllPosesFromTree()

    all_poses_from_tree = list(getAllPosesFromTree())
    logger.info(f"Saving {len(all_poses_from_tree)} files")
    logger.info(all_poses_from_tree)

    with open(rpy_outpath, "w") as rpyfp:
        for pose in getAllPosesFromTree():
            pose.saveImage()
            rpyfp.write(pose.rpy_definition)

    if make_demo:
        logger.info(f"Saving demos")
        for pose in getAllPosesFromTree():
            out_path_demo = pose.out_filepath_real.replace("rpydiff_out", "rpydiff_out_demo")
            ensurePath(out_path_demo)
            logger.debug(f"Saving {pose} demo")
            if pose.image:
                pose.getImage().save(out_path_demo)


def poseFromFile(posefilepath):
    a, b = os.path.split(posefilepath)
    char_name = os.path.split(a)[1]
    file_plainname, file_ext = os.path.splitext(b)
    subposes = re.split(r"[ _-]", file_plainname)
    if PREFIXED_WITH_NAME:
        return Pose(char_name, subposes[1:]).loadImage(posefilepath)
    else:
        return Pose(char_name, subposes).loadImage(posefilepath)


def posesFromDir(sprite_dir):
    all_poses = []
    for posefilepath in glob.glob(os.path.join(sprite_dir, "*.png")):
        a, b = os.path.split(posefilepath)
        char_name = os.path.split(a)[1]
        file_plainname, file_ext = os.path.splitext(b)
        subposes = re.split(r"[ _-]", file_plainname)
        all_poses.append(Pose(char_name, subposes).loadImage(posefilepath))
    return all_poses


def poseToDict(inpose):
    return {
        dkey: inpose.__getattribute__(okey)
        for dkey, okey in Pose.api.items()
        if inpose.__getattribute__(okey)
    }


def poseFromDict(name, indict):
    p = Pose(name, indict["pose"])
    for dkey, value in indict.items():
        p.__setattr__(Pose.api[dkey], value)
    p.loadImage(indict["source"])
    return p


def posesFromYaml(yaml_path):
    with open(yaml_path, "r") as fp:
        all_poses_def = yaml.safe_load(fp)
    all_poses = []
    for name, poses in all_poses_def.items():
        for pd in poses:
            all_poses.append(poseFromDict(name, pd))
    return (name, all_poses)


def dumpPosesToYaml(name, all_poses, yaml_out_path):
    logger.info(f"Dumping pose data to '{yaml_out_path}'")
    data = {name: [poseToDict(p) for p in all_poses]}
    with open(yaml_out_path, "w") as fp:
        yaml.dump(data, fp)


def main():
    import argparse
    ap = argparse.ArgumentParser()

    def add_bool_arg(parser, name, default=True, help=None):
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument('--' + name, dest=name.replace("-", "_"), action='store_true', help=help + f" (Default: {default})")
        group.add_argument('--no-' + name, dest=name.replace("-", "_"), action='store_false', help=help + f" (Default: {default})")
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
        '--character-defs', nargs="+", default=[],
        help="Character definitions, in yaml files"
    )
    ap.add_argument(
        "--rpy-out", default=None,
        help="Output rpy filename"
    )
    ap.add_argument(
        "--fuzz", default=100, type=int,
        help="Fuzzing amount"
    )
    ap.add_argument(
        "--efficiency-threshhold", dest="efficiency_threshhold", default=0.5, type=float,
        help="Efficiency threshhold"
    )

    add_bool_arg(ap, "trim", default=False, help="Remove whitespace from around sprites")
    add_bool_arg(ap, "clean", default=True, help="Remove old versions in outdir")
    add_bool_arg(ap, "patch", default=True, help="Generate patches to compress character sprites")
    add_bool_arg(ap, "dump-yaml", default=False, help="Dump generated sprite data to yaml, for editing")
    add_bool_arg(ap, "make-demo", default=False, help="Create a demo of what the final sprites will look like after patched")

    add_bool_arg(ap, "threaded", default=False, help="Use threads for faster processing")

    args = ap.parse_args()

    global use_threading
    use_threading = args.threaded
    global fuzz
    fuzz = args.fuzz
    global REPLACE_THRESHHOLD
    REPLACE_THRESHHOLD = args.efficiency_threshhold
    
    for sprite_dir in args.character_dirs:
        all_poses = [
            poseFromFile(pngfile)
            for pngfile in glob.glob(os.path.join(sprite_dir, "*.png"))
        ]
        logger.info(f"Loaded {len(all_poses)} poses from directory '{sprite_dir}'")
        
        sprite_name_auto = os.path.split(os.path.split(os.path.join(sprite_dir, ""))[0])[1]  # sorry

        if args.dump_yaml:
            yaml_out_path = os.path.join("rpydiff_out", args.rpy_out or sprite_name_auto + ".yaml")
            dumpPosesToYaml(sprite_name_auto, all_poses, yaml_out_path)

        if args.clean:
            for kkk in [all_poses[0].out_filepath_real, all_poses[0].out_filepath_real.replace("rpydiff_out", "rpydiff_out_demo")]:
                outdir, __ = os.path.split(kkk)
                logger.info(f"Remove old {outdir}")
                for path in glob.glob(os.path.join(outdir, "*.*")):
                    os.unlink(path)

        rpy_outpath = os.path.join("rpydiff_out", args.rpy_out or sprite_name_auto + ".rpy")
        ppargs = (all_poses, args.trim, args.patch, rpy_outpath, args.make_demo)
        if use_threading:
            new_thread = threading.Thread(target=processPoses, args=ppargs)
            LAZY_THREADS.append(new_thread)
            new_thread.start()
        else:
            processPoses(*ppargs)

    for yaml_path in args.character_defs:
        char_name, all_poses = posesFromYaml(yaml_path)
        logger.info(f"Loaded {len(all_poses)} poses from file '{yaml_path}'")

        rpy_outpath = os.path.join("rpydiff_out", args.rpy_out or char_name + ".rpy")
        ppargs = (all_poses, args.trim, args.patch, rpy_outpath, args.make_demo)
        if use_threading:
            new_thread = threading.Thread(target=processPoses, args=ppargs)
            LAZY_THREADS.append(new_thread)
            new_thread.start()
        else:
            processPoses(*ppargs)

    # Start all LAZY_THREADS
    # for thread in LAZY_THREADS:
    #     thread.start()

    # Wait for all of them to finish
    for thread in LAZY_THREADS:
        thread.join()


if __name__ == "__main__":
    main()
    for thread in LAZY_THREADS:
        thread.join()
