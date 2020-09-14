import os
import shutil
import json

# This is just a helper program that generates empty packages for you

CUSTOM_VOLUMES = "../../custom_volumes/"


def makeEmptyPackage(package_id):
    pkg_dir = os.path.join(CUSTOM_VOLUMES, package_id)
    os.makedirs(pkg_dir)
    os.makedirs(os.path.join(pkg_dir, "assets"))
    meta = {
        "package_id": package_id,
        "volumes": [
            {
                "volume_id": "vol",
                "title": "Volume",
                "subtitle": "Subtitle"
            }
        ]
    }
    with open(os.path.join(pkg_dir, "meta.json"), "w") as fp:
        json.dump(meta, fp, indent=4)
    with open(os.path.join(pkg_dir, "route.rpy"), "w") as fp:
        fp.write("init offset = 3\n\n")
        fp.write("label __package_entrypoint___vol:\n")
        fp.write("    \n")
        fp.write("    return\n\n")


if __name__ == "__main__":
    import sys
    for package_id in sys.argv[1:]:
        makeEmptyPackage(package_id)
