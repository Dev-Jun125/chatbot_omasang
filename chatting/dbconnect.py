from os import stat_result
import pymysql
from pymysql import NULL, cursors
import yaml

class SqlCommunication:
    def __init__(self):
        with open('c:/Users/thdnf/OneDrive/바탕 화면/omasang/chatbot/chantest/hanseo_chatbot/connection_information.yaml', encoding = 'UTF-8') as connect_inf:
            information_deployment = yaml.load(connect_inf, Loader=yaml.FullLoader)
        info = information_deployment
        self.db = pymysql.connect(
        user = info['user'],
        passwd = info['passwd'],
        host = info['host'],
        db = info['db'],
        charset = info['charset']
        )
        
        self.cursor = self.db.cursor()
    
    def execute(self, query, values):
        self.cursor.execute(query, values)
    
    def executemany(self, query, values):
        self.cursor.executemany(query, values)

    def fetchone(self, query, values):
        self.cursor.execute(query, values)
        row = self.cursor.fetchone()
        return row

    def fetchall(self, query, values):
        self.cursor.execute(query, values)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
    
    def close(self):
        self.db.close()
    


    

   