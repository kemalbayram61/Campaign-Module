from Abstracts.DBConstants import DBConstants
from Objects.Campaign import Campaign
import psycopg2

class DBHelper:
    __database: str
    __user: str
    __password: str
    __host: str
    __port: str
    __connection = None

    def __init__(self, database:str = None,
                 user:str = None,
                 password:str = None,
                 host:str = None,
                 port:str = None):
        self.__database = database
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.checkVersion()

    def connect(self):
        self.__connection = psycopg2.connect(database=self.__database,
                                             user=self.__user,
                                             password=self.__password,
                                             host=self.__host,
                                             port=self.__port)

    def disconnect(self):
        self.__connection.close()

    def checkVersion(self):
        self.connect()
        cursor = self.__connection.cursor()
        cursor.execute("select version()")
        result = cursor.fetchone()
        print(result)
        self.disconnect()

    def resetTables(self):
        self.connect()
        cursor = self.__connection.cursor()
        cursor.execute("drop table if exists " + DBConstants.CAMPAIGN_TABLE_NAME.value)
        cursor.execute("drop table if exists " + DBConstants.PRODUCT_TABLE_NAME.value)
        cursor.execute("drop table if exists " + DBConstants.CONDITIONAL_SELECTION_TABLE_NAME.value)
        cursor.execute("drop table if exists " + DBConstants.PRODUCT_FEATURE_TABLE_NAME.value)

        campaignSql = '''
            create table {}(
                _id serial primary key,
                name varchar(60) NOT NULL,
                productFilter int NOT NULL,
                productFilterCriteria varchar(500) NOT NULL,
                conditionalSelectionID int
            )
        '''.format(DBConstants.CAMPAIGN_TABLE_NAME.value)
        productSql = '''
            create table {}(
                _id serial primary key,
                name varchar(60) NOT NULL
            )
        '''.format(DBConstants.PRODUCT_TABLE_NAME.value)
        productFeatureSql = '''
            create table {}(
                productID int NOT NULL,
                feature varchar(60) NOT NULL
            )
        '''.format(DBConstants.PRODUCT_FEATURE_TABLE_NAME.value)
        conditionalSelectionSql = '''
            create table {}(
                _id serial primary key,
                campaignID int NOT NULL,
                requiredType int NOT NULL,
                requiredCriteria varchar(500) NOT NULL,
                requiredCount int NOT NULL,
                redundantType int NOT NULL,
                redundantCriteria varchar(500) NOT NULL,
                redundantCount int NOT NULL
            )
        '''.format(DBConstants.CONDITIONAL_SELECTION_TABLE_NAME.value)

        cursor.execute(campaignSql)
        cursor.execute(productSql)
        cursor.execute(productFeatureSql)
        cursor.execute(conditionalSelectionSql)
        self.__connection.commit()
        self.disconnect()

    def insertCampaign(self, campaign: Campaign):
        self.connect()
        cursor = self.__connection.cursor()
        sql = '''
            insert into {}(
                name,
                productFilter,
                productFilterCriteria,
                conditionalSelectionID) values ('{}', {}, '{}', {})
        '''.format(DBConstants.CAMPAIGN_TABLE_NAME.value, campaign.getName(), campaign.getProductFilter().value, str(campaign.getProductFilterCriteria()), int(campaign.getConditionalSelectionID()))
        cursor.execute(sql)
        self.__connection.commit()
        self.disconnect()
