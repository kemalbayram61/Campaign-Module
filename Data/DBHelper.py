from Data.Config import Config
import psycopg2

class DBHelper:
    connection = None
    cursor = None
    config: Config = None

    def __init__(self):
        self.config = Config()
        self.open_connection()

    def select_one(self, table_name: str):
        self.cursor.execute("select * from " + table_name)
        result = self.cursor.fetchone()
        return result

    def select_all(self, table_name: str):
        self.cursor.execute("select * from " + table_name)
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        self.connection.close()

    def open_connection(self):
        self.connection = psycopg2.connect( database=self.config.get_db_name(),
                                            user=self.config.get_db_user(),
                                            host=self.config.get_db_host(),
                                            port=self.config.get_db_port())
        self.cursor = self.connection.cursor()
        self.cursor.execute("select version()")
        data = self.cursor.fetchone()
        print("Connection established to: ",data)