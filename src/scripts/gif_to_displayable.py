from PIL import Image
import os


def explodeGif(gif_path):
    im = Image.open(gif_path)
    __, gifname = os.path.split(gif_path)
    name, __ = os.path.splitext(gifname)

    os.makedirs(name, exist_ok=True)

    try:
        while True:
            frame = im.tell() 
            outpath = os.path.join(name, f"{frame}.png")
            im.save(outpath)
            im.seek(frame + 1)
    except EOFError:
        return


def makeGifDef(gif_path):
    im = Image.open(gif_path)
    __, gifname = os.path.split(gif_path)
    name, __ = os.path.splitext(gifname)

    _assets_ = r"{{assets}}"

    with open(f"{name}.rpy", "w") as fp:
        fp.write(f"image !{name}:\n")
        try:
            while True:
                frame = im.tell() 
                duration = im.info['duration']

                fp.write(f'\tImage("' + _assets_ + f'/gifs/{name}/{frame}.png")\n')
                fp.write(f"\tpause {duration/1000}\n")

                im.seek(frame + 1)
        except EOFError:
            pass
        fp.write("\trepeat\n\n")
    return


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "gif",
        help="Input file")
    args = ap.parse_args()

    explodeGif(args.gif)
    makeGifDef(args.gif)


if __name__ == "__main__":
    main()
