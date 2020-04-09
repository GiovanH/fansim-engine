"""Summary

Attributes:
    indir (str): Description
    outdir (str): Description
    patchmode_default (str): Description
    rpy_preamble (TYPE): Description
    SEP (str): Description
"""
from PIL import Image
from PIL import ImageChops
import shutil
# from PIL import ImageChops
import os
import glob
import math
import sys

# N.B. Unlike most other scripts, this requires Python 3.8.
# If you run this with an outdated python version, you will get a SyntaxError.
# This script is entirely optional.


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
        

def spriteTrim(pngpath):
    png_dir, png_filename = os.path.split(pngpath)
    png_plainname, png_ext = os.path.splitext(png_filename)
    print(png_plainname)

    sprite_image = Image.open(pngpath).convert('RGBA')

    bbox_orig = (0, 0, *sprite_image.size)
    bbox_real = sprite_image.getbbox()

    if bbox_orig == bbox_real:
        # Clean transparency
        pixdata = sprite_image.load()
        if pixdata[0, 0] != (0, 0, 0, 0):
            for y in range(sprite_image.size[1]):
                for x in range(sprite_image.size[0]):
                    if pixdata[x, y][3] == 0:
                        pixdata[x, y] = (0, 0, 0, 0)
        bbox_real = sprite_image.getbbox()
        if bbox_orig == bbox_real:
            return
        
    bakpath = os.path.join(png_dir, f"{png_plainname}{png_ext}.bak")
    if not os.path.isfile(bakpath):
        shutil.copy2(pngpath, bakpath)

    bbox_mirrored = (
        min(bbox_real[0], bbox_orig[2] - bbox_real[2]),
        bbox_real[1],
        max(bbox_real[2], bbox_orig[3] - bbox_real[3]),
        bbox_orig[3]
    )

    if bbox_orig == bbox_mirrored:
        return
    
    print(bbox_orig)
    print(bbox_real)
    print(bbox_mirrored)
    # (454, 42, 938, 720)
    # (342, 43, 938, 720)

    bounded_image = sprite_image.crop(bbox_mirrored)
    bounded_image.save(pngpath)

    globals().update(locals())

    return 

if __name__ == '__main__':
    indir = sys.argv[1]
    for pngpath in glob.glob(os.path.join(indir, "*.png")):
        spriteTrim(pngpath)
