from PIL import Image
import os


def explodeGif(gif_path):
    im = Image.open(gif_path)
    __, gifname = os.path.split(gif_path)
    name, __ = os.path.splitext(gifname)

    os.makedirs(os.path.join("gifs", name), exist_ok=True)

    try:
        while True:
            frame = im.tell() 
            outpath = os.path.join("gifs", name, f"{frame}.png")
            im.save(outpath)
            im.seek(frame + 1)
    except EOFError:
        return


def makeGifDef(gif_path):
    im = Image.open(gif_path)
    __, gifname = os.path.split(gif_path)
    name, __ = os.path.splitext(gifname)

    _assets_ = r"{{assets}}"
    os.makedirs(name, exist_ok=True)

    with open(f"{name}.rpy", "w") as fp:
        fp.write(f"image !{name}:\n")
        last_frame_data = None
        duration = 0

        try:
            while True:
                frame = im.tell()
                this_frame_data = list(im.getdata())
                
                if last_frame_data != this_frame_data:
                    im.save(os.path.join(name, f"{frame}.png"))
                    if duration:
                        fp.write(f"    pause {duration/1000}\n")
                    fp.write(f'    Image("' + _assets_ + f'/gifs/{name}/{frame}.png")\n')
                    duration = 0

                duration += im.info['duration']
                last_frame_data = this_frame_data

                im.seek(frame + 1)
        except EOFError:
            fp.write(f"    pause {duration/1000}\n")
        fp.write("    repeat\n\n")
    return


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "gif",
        help="Input file")
    args = ap.parse_args()

    # explodeGif(args.gif)
    makeGifDef(args.gif)


if __name__ == "__main__":
    main()
