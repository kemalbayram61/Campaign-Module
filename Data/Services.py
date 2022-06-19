from Data.DBHelper import DBHelper
from Abstracts.DBConstants import DBConstants
from Abstracts.EnvConstants import EnvConstants
from Objects.Campaign import Campaign
from Objects.Product import Product
from Objects.ConditionalSelection import ConditionalSelection

class Services:
    __envs :dict = None
    __dbHelper: DBHelper = None
    def __init__(self):
        self.loadEnvs()
        self.__dbHelper = DBHelper(database=self.__envs[DBConstants.DATABASE.value].replace('\n', ''),
                                   user=self.__envs[DBConstants.USER.value].replace('\n', ''),
                                   password=self.__envs[DBConstants.PASSWORD.value].replace('\n', ''),
                                   host=self.__envs[DBConstants.HOST.value].replace('\n', ''),
                                   port=self.__envs[DBConstants.PORT.value].replace('\n', ''))

        if(self.__envs[EnvConstants.RESET_TABLES_ON_INIT.value] == "1"):
            self.__dbHelper.resetTables()

    def getSelectedEnv(self) ->str:
        mainEnvFile = open("Config/main.env")
        for line in mainEnvFile.readlines():
            if ("#" not in line and line.split("=", 1)[0] == EnvConstants.SELECTED_ENVIRONMENT.value):
                return line.split("=", 1)[1]
        return "local"

    def loadEnvs(self):
        self.__envs = {}
        envsFile = open("Config/" + self.getSelectedEnv() + ".env")
        for line in envsFile.readlines():
            if ("#" not in line and line != '\n'):
                self.__envs[line.split("=", 1)[0]] = line.split("=", 1)[1]

    def insertCampaign(self, campaign: Campaign):
        self.__dbHelper.insertCampaign(campaign)

    def insertProduct(self, product: Product):
        self.__dbHelper.insertProduct(product)

    def insertConditionalSelection(self, conditionalSelection: ConditionalSelection):
        self.__dbHelper.insertConditionalSelection(conditionalSelection)

    def getAllCampaign(self):
        allCampaign = self.__dbHelper.select(DBConstants.CAMPAIGN_TABLE_NAME)
        print(allCampaign)

    def getAllProduct(self):
        allProduct = self.__dbHelper.select(DBConstants.PRODUCT_TABLE_NAME)
        print(allProduct)

    def getAllConditionalSelection(self):
        allCconditionalSelection = self.__dbHelper.select(DBConstants.CONDITIONAL_SELECTION_TABLE_NAME)
        print(allCconditionalSelection)