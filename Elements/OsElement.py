from Elements.BaseElement import BaseElement
from pathlib import Path
import os


class OsFile(BaseElement):

    def __init__(self, by_: str, locator: str, name: str):
        super(OsFile, self).__init__(by_, locator, name)

    def is_file_exists(self):
        filepath_real = Path(os.path.dirname(os.path.realpath(__file__)))
        script_dir = str(filepath_real.parent)
        return os.path.exists(f'{script_dir}/sampleFile.jpeg')
