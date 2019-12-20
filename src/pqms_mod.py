import os
import json
import glob
import yaml

from patcher import subtableReplace

class Package(object):

    def __init__(self, package_dir):
        super().__init__()
        self.root = package_dir

        self.loadMetadata()
        self.loadCredits()

    @property
    def id(self):
        return self.metadata["package_id"]

    @property
    def public(self):
        return self.metadata.get("public", False)

    @property
    def private(self):
        return not self.public

    @property
    def volumes(self):
        return self.metadata["volumes"]

    @property
    def assets_dir(self):
        return os.path.join(self.root, "assets")
    
    @property
    def assets_common_dir(self):
        return os.path.join(self.root, "assets_common")

    def loadMetadata(self):
        meta_filepath = os.path.join(self.root, "meta.json")
        with open(meta_filepath, "r", encoding="utf-8") as fp:
            self.metadata = json.load(fp)

        for volume in self.metadata["volumes"]:
            volume["package_id"] = self.id

    def loadCredits(self):
        credits_filepath = os.path.join(self.root, "credits.yml")
        if os.path.isfile(credits_filepath):
            with open(credits_filepath, "r", encoding="utf-8") as fp:
                self.credits = yaml.safe_load(subtableReplace(fp.read(), self.metadata))
        else:
            self.credits = None

    def getScriptFiles(self):
        for rpy in glob.glob(os.path.join(self.root, "*.rpy")):
            yield rpy

    def getArchiveFiles(self):
        for rpa in glob.glob(os.path.join(self.root, "*.rpa")):
            yield rpa


if __name__ == "__main__":
    # test
    betas = Package("../custom_volumes_other/pq_betas/")
    openb = Package("../custom_volumes_other/openbound/")
