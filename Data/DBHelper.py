from Abstracts.DBConstants import DBConstants
from Objects.Campaign import Campaign
from Objects.Product import Product
from Objects.DBFilter import DBFilter
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

        campaignSql = '''
            create table {}(
                _id serial primary key,
                name varchar(100) NOT NULL,
                companyID int NOT NULL,
                productFilter int,
                productFilterCriteria json,
                implementationType int,
                implementationTypeCriteria int,
                implementationTypeAmount decimal,
                requiredType int,
                requiredCriteria json,
                requiredCount int,
                requiredCondition int,
                requiredConditionAmount decimal,
                redundantType int,
                redundantCriteria json,
                redundantCondition int,
                redundantConditionAmount decimal,
                redundantCount int)'''.format(DBConstants.CAMPAIGN_TABLE_NAME.value)
        productSql = '''
            create table {}(
                _id serial primary key,
                name varchar(60) NOT NULL,
                features json NOT NULL
            )
        '''.format(DBConstants.PRODUCT_TABLE_NAME.value)

        cursor.execute(campaignSql)
        cursor.execute(productSql)
        self.__connection.commit()
        self.disconnect()

    def insertCampaign(self, campaign: Campaign):
        self.connect()
        cursor = self.__connection.cursor()
        sql = f'''
            insert into {DBConstants.CAMPAIGN_TABLE_NAME.value}(
                name,
                companyID,
                productFilter,
                productFilterCriteria,
                implementationType ,
                implementationTypeCriteria ,
                implementationTypeAmount ,
                requiredType ,
                requiredCriteria ,
                requiredCount,
                requiredCondition,
                requiredConditionAmount,
                redundantType,
                redundantCriteria,
                redundantCondition,
                redundantConditionAmount,
                redundantCount) values ('
                {campaign.getName()}', 
                {int(campaign.getCompanyID())} , 
                { 'NULL' if campaign.getProductFilter() == None else campaign.getProductFilter().value}, 
                '{{"criteria":{str(0 if campaign.getProductFilterCriteria() == None else campaign.getProductFilterCriteria())}}}',
                {'NULL' if campaign.getImplementationType() == None else campaign.getImplementationType().value},
                {'NULL' if campaign.getImplementationTypeCriteria() == None else campaign.getImplementationTypeCriteria().value},
                {'NULL' if campaign.getImplementationTypeAmount() == None else campaign.getImplementationTypeAmount()},
                {'NULL' if campaign.getRequiredType() == None else campaign.getRequiredType().value},
                '{{"criteria":{str(0 if campaign.getRequiredCriteria() == None else campaign.getRequiredCriteria())}}}',
                {'NULL' if campaign.getRequiredCount() == None else campaign.getRequiredCount()},
                {'NULL' if campaign.getRequiredCondition() == None else campaign.getRequiredCondition().value},
                {'NULL' if campaign.getRequiredConditionAmount() == None else campaign.getRequiredConditionAmount()},
                {'NULL' if campaign.getRedundantType() == None else campaign.getRedundantType().value},
                '{{"criteria":{str(0 if campaign.getRedundantCriteria() == None else campaign.getRedundantCriteria())}}}',
                {'NULL' if campaign.getRedundantCondition() == None else campaign.getRedundantCondition().value},
                {'NULL' if campaign.getRedundantConditionAmount() == None else campaign.getRedundantConditionAmount()},
                {'NULL' if campaign.getRedundantCount() == None else campaign.getRedundantCount()})
        '''

        cursor.execute(sql)
        self.__connection.commit()
        self.disconnect()

    def insertProduct(self, product: Product):
        self.connect()
        cursor = self.__connection.cursor()
        featuresStr: str = "[" + ','.join([str(elem) for elem in product.getFeatures()]) + "]"
        sql = f'''
            insert into {DBConstants.PRODUCT_TABLE_NAME.value}(
                name,
                features) values ('{product.getname()}', '{{"features":{featuresStr}}}')
        '''

        cursor.execute(sql)
        self.__connection.commit()
        self.disconnect()

    def select(self, tableName: DBConstants, criteria: list[DBFilter] = None):
        self.connect()
        cursor = self.__connection.cursor()
        sql = "select * from " + str(tableName.value)
        if(criteria is not None and len(criteria)>0):
            sql = sql + " where " + ' and '.join([str(elem.key) + str(elem.operator) + str(elem.value) for elem in criteria])
        cursor.execute(sql)
        result = cursor.fetchall()
        self.disconnect()
        return result
