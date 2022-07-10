from Data.Config import Config
import psycopg2

class DBHelper:
    connection = None
    cursor = None
    config: Config = None

    def __init__(self):
        self.config = Config()
        self.open_connection()
        if(self.config.get_reset_table_on_init()):
            self.reset_tables()

    def reset_tables(self) ->None:
        self.cursor.execute("drop table if exists product")
        self.cursor.execute("drop table if exists campaign")
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
        self.cursor.execute(product_sql)
        self.connection.commit()

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