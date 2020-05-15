import os
from PIL import Image
import base64
import random


# def _rot(s, n):
#     n2 = n * 2
#     d = {i + c: ((i + n) % n2 + c) for c in (0, n2) for i in range(n2)}
#     print(n, d)
#     print(s)
#     return "".join([str(d.get(c, c)) for c in s])


def getBindata(image_path):
    with open(image_path, "rb") as fp:
        bindata = fp.read()
    return bindata


def imageToRpy(image_path, rpy_out_path):
    filename, ext = os.path.splitext(filepath)
    # out_filepath = f"{filename}_obs{ext}"

    bindata = getBindata(image_path)
    globals().update(locals())

    n = random.randint(10, 20)
    data = base64.b64encode(bindata)
    print(data)

    rpy_out_fp = open(rpy_out_path, "w")
    # rpy_out_fp.write("init python:\n\timport base64\n\n")
    rpy_out_fp.write(f"image !{filename} = fseObsImData({data}, \"{filename}{ext}\")\n")
    rpy_out_fp.close()


if __name__ == "__main__":
    import sys
    for filepath in sys.argv[1:]:
        filename, ext = os.path.splitext(filepath)
        imageToRpy(filepath, f"{filename}.rpy")
