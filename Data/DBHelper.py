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
        self.test()

    def connect(self):
        self.__connection = psycopg2.connect(database=self.__database,
                                             user=self.__user,
                                             password=self.__password,
                                             host=self.__host,
                                             port=self.__port)

    def test(self):
        self.connect()
        cursor = self.__connection.cursor()
        cursor.execute("select version()")
        result = cursor.fetchone()
        print(result)
        self.disconnect()

    def disconnect(self):
        self.__connection.close()