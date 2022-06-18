class Services:
    __envs :list[list[str]] = None

    def __init__(self):
        self.loadEnvs()

    def getSelectedEnv(self) ->str:
        mainEnvFile = open("Config/main.env")
        for line in mainEnvFile.readlines():
            if ("#" not in line and line.split("=", 1)[0] == "SELECTED_ENVIRONMENT"):
                return line.split("=", 1)[1]
        return "local"

    def loadEnvs(self):
        self.__envs = []
        envsFile = open("Config/" + self.getSelectedEnv() + ".env")
        for line in envsFile.readlines():
            if ("#" not in line):
                self.__envs.append(line.split("=", 1))
        print(self.__envs)