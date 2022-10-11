import logging
from pathlib import Path
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

filepath_real = Path(os.path.dirname(os.path.realpath(__file__)))
script_dir = str(filepath_real.parent)
rel_path = f'{script_dir}\data'

file_handler = logging.FileHandler(f'{rel_path}\TestLog.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)