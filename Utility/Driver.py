from Utility.BrowserFactory import BrowserFacory
from Utility.DataUtility import Data


class BrowserUtils():

    _instances = {}

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = BrowserFacory.BrwoserFactory(
                Data.data_access(f"{chr(92)}ConfigData.json", "Browser", "BrowserName", 1))

        return cls._instances[cls]

    @classmethod
    def clear(cls):
        cls._instances = {}

    @classmethod
    def quit(cls):
        cls._instances.quit()

    @classmethod
    def return_instance(cls):
        return BrowserUtils()





'''
from Utility.BrowserFactory import BrowserFacory
from Utility.DataUtility import Data


class SingletonMetaclass(type):
    def __del__(self):
        print("Object deleted")

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = BrowserFacory.BrwoserFactory(
                Data.data_access(f"{chr(92)}ConfigData.json", "Browser", "BrowserName", 1))

        return cls.instance


class Singleton(SingletonMetaclass):

    def return_instance():
        return SingletonMetaclass()
'''