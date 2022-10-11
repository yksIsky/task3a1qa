import json
import os
from pathlib import Path


class Data():

    @staticmethod
    def data_access(file_name: str, groupe: str, row_key: str, id):
        filepath_real = Path(os.path.dirname(os.path.realpath(__file__)))
        script_dir = str(filepath_real.parent)
        rel_path = f'{script_dir}\data{file_name}'
        with open(rel_path, "r") as data:
            ConfigData = json.load(data)

        return "".join([str(field[row_key]) for field in ConfigData[groupe] if field["id"] == id])

    @staticmethod
    def write(file_name: str, key: str, column: str, value: list):
        filepath_real = Path(os.path.dirname(os.path.realpath(__file__)))
        script_dir = str(filepath_real.parent)
        rel_path = f'{script_dir}\data{file_name}'
        with open(rel_path, "r") as data:
            ConfigData = json.load(data)

        ConfigData[key].append({"id": len(ConfigData[key]) + 1, column: value})

        with open(rel_path, "w") as outfile:
            json.dump(ConfigData, outfile)

    @staticmethod
    def open(file_name: str):
        filepath_real = Path(os.path.dirname(os.path.realpath(__file__)))
        script_dir = str(filepath_real.parent)
        rel_path = f'{script_dir}\data{file_name}'
        with open(rel_path, "r") as data:
            ConfigData = json.load(data)

        return ConfigData

    @staticmethod
    def get_test_data():
        data = Data.open(f"{chr(92)}ddt.json")
        user_data = []
        for lists in range(len(data['Test1'])):
            user_data.append(tuple(data['Test1'][0].values()))

        return user_data
