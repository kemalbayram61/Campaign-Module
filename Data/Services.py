from Data.DBHelper import DBHelper
from Objects.Campaign import Campaign
class Services:
    __envs :dict = None
    __dbHelper: DBHelper = None
    def __init__(self):
        self.loadEnvs()
        self.__dbHelper = DBHelper(self.__envs["CONNECTION_STRING"], self.__envs["DATABASE_NAME"])

    def getSelectedEnv(self) ->str:
        mainEnvFile = open("Config/main.env")
        for line in mainEnvFile.readlines():
            if ("#" not in line and line.split("=", 1)[0] == "SELECTED_ENVIRONMENT"):
                return line.split("=", 1)[1]
        return "local"

    def loadEnvs(self):
        self.__envs = {}
        envsFile = open("Config/" + self.getSelectedEnv() + ".env")
        for line in envsFile.readlines():
            if ("#" not in line):
                self.__envs[line.split("=", 1)[0]] = line.split("=", 1)[1]