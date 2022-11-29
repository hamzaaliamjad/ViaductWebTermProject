import config
import pymysql


hostStr = config.DB_IP
userStr = config.DB_USER
passStr = config.DB_PASSWORD
DB = config.DATABASE


class DBHandler:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=hostStr, user=userStr, password=passStr, database=DB)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(str(e))

    def __del__(self):
        try:
            if not self.cursor is None:
                self.cursor.close()
            if not self.conn is None:
                self.conn.close()
        except Exception as e:
            print(str(e))
