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
            id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
            barcode varchar(20) NOT NULL,
            criteria_campaign_list varchar(100),
            action_campaign_list varchar(100),
            org_id varchar(100)
            )
        '''
        customer_sql: str = '''
            create table customer(
            id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
            campaign_list varchar(100),
            org_id varchar(100)
            )
        '''

        payment_channel_sql: str = '''
            create table payment_channel(
            id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
            campaign_list varchar(100),
            org_id varchar(100)
            )
        '''

        payment_type_sql: str = '''
            create table payment_type(
            id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
            campaign_list varchar(100),
            org_id varchar(100)
            )
        '''

        campaign_sql: str = '''
            create table campaign(
            id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
            level int NOT NULL,
            start_date varchar(30),
            end_date varchar(30),
            min_qty int,
            min_amount real,
            max_occurrence int,
            action_type int,
            action_amount real,
            action_qty int,
            max_discount real,
            is_active int,
            all_payment_channel int, 
            all_customer int, 
            all_payment_type int, 
            all_product_criteria int, 
            all_product_action int,
            org_id varchar(100)
            )
        '''

        self.cursor.execute(product_sql)
        self.cursor.execute(customer_sql)
        self.cursor.execute(payment_channel_sql)
        self.cursor.execute(payment_type_sql)
        self.cursor.execute(campaign_sql)
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

    def select_all_by_org_id(self, table_name: str, org_id: str):
        self.open_connection()
        self.cursor.execute("select * from " + table_name + " where org_id='" + org_id + "'")
        result = self.cursor.fetchall()
        self.close_connection()
        return result

    def find_by_id(self, table_name: str, id: str):
        self.open_connection()
        self.cursor.execute("select * from " + table_name + " where id='" + id + "'")
        result = self.cursor.fetchone()
        self.close_connection()
        return result

    def find_product_by_barcode(self, barcode: str):
        self.open_connection()
        self.cursor.execute("select * from product where barcode='"+ barcode + "'")
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
        print("Connection established to: " + str(data))