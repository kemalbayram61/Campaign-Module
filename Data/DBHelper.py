from Data.Config import Config
from Mock.Product import ProductMock
import psycopg2

class DBHelper:
    connection = None
    cursor = None
    config: Config = None

    def __init__(self):
        self.config = Config()

    def reset_tables(self) ->None:
        self.open_connection()
        self.cursor.execute("drop table if exists product")
        self.cursor.execute("drop table if exists customer")
        self.cursor.execute("drop table if exists campaign")
        self.cursor.execute("drop table if exists payment_channel")
        self.cursor.execute("drop table if exists payment_type")

        product_sql: str = '''
            create table product(
            id SERIAL NOT NULL PRIMARY KEY,
            name varchar(60) NOT NULL,
            barcode varchar(20) NOT NULL,
            property json NOT NULL,
            criteria varchar(100),
            action varchar(100),
            amount real
            )
        '''
        customer_sql: str = '''
            create table customer(
            id SERIAL NOT NULL PRIMARY KEY,
            name varchar(60) NOT NULL,
            property json NOT NULL,
            campaign_list varchar(100)
            )
        '''

        payment_channel_sql: str = '''
            create table customer(
            id SERIAL NOT NULL PRIMARY KEY,
            name json NOT NULL,
            campaign_list varchar(100)
            )
        '''

        payment_type_sql: str = '''
            create table customer(
            id SERIAL NOT NULL PRIMARY KEY,
            name json NOT NULL,
            campaign_list varchar(100)
            )
        '''

        self.cursor.execute(product_sql)
        self.cursor.execute(customer_sql)
        self.cursor.execute(payment_channel_sql)
        self.cursor.execute(payment_type_sql)
        self.connection.commit()
        self.close_connection()

    def execute_command(self, command: str):
        self.open_connection()
        self.cursor.execute(command)
        self.connection.commit()
        self.close_connection()

    def select_one(self, table_name: str):
        self.open_connection()
        self.cursor.execute("select * from " + table_name)
        result = self.cursor.fetchone()
        self.close_connection()
        return result

    def select_all(self, table_name: str):
        self.open_connection()
        self.cursor.execute("select * from " + table_name)
        result = self.cursor.fetchall()
        self.close_connection()
        return result

    def find_by_id(self, table_name: str, id: str):
        self.open_connection()
        self.cursor.execute("select * from " + table_name + " where id="+ id)
        result = self.cursor.fetchone()
        self.close_connection()
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