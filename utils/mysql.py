import pymysql
from .function import create_insert_sql,create_update_sql
from . import SQLConfig


class MySqldb(object):
    def __init__(self):
        self.db = pymysql.connect(SQLConfig.SQL_ADDRESS,SQLConfig.SQL_USERNAME,\
            SQLConfig.SQL_PASSWORD,SQLConfig.SQL_DATABASE)

    # 一共就四个方法，增删改查。
    # 增，也就是insert
    # 增加一共有两个变量，一个是需要增加到哪个表里面去，另一个是数据。
    def insert(self, table, values):
        cursor = self.db.cursor()
        #  获取表头数据，保证数据顺序
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s'"%(table)
        cursor.execute(sql)
        table_name = cursor.fetchall()
        table_column = {}
        for i in table_name:
            table_column[i[0]] = ''
        values = {**table_column,**values}
        #  创建sql
        sql = "INSERT INTO %s VALUES %s"%(table,create_insert_sql(values))
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            print('insert fail')

    #  删除，变量只有两个
    #  表名， 条件
    def delete(self, table, condition):
        cursor = self.db.cursor()
        sql = "DELETE FROM %s WHERE %s = '%s'" % \
            (table,list(condition.keys())[0],condition[list(condition.keys())[0]])
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            print('delete fail')


    #  改
    #  传入参数依次为，表名，需要修改的值， 寻找条件
    def update(self, table, values, condition):
        cursor = self.db.cursor()
        sql = "UPDATE %s SET %s WHERE %s = '%s'"%\
            (table,create_update_sql(values),list(condition.keys())[0],condition[list(condition.keys())[0]])
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            print("update fail")        


    # 全查
    # 传入参数依次：表名
    def list_all(self, table):
        cursor = self.db.cursor()
        #  获取当前表头
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s'"%(table)
        cursor.execute(sql)
        table_name = cursor.fetchall()
        table_column = []
        for i in table_name:
            table_column.append(i[0])
        
        sql = "SELECT * FROM %s" % (table)
        try:
            cursor.execute(sql)
            table_data = []
            data = cursor.fetchall()
            for i in data:
                table_data.append(dict(zip(table_column,list(i))))
            return table_data
        except:
            print('get fail')


    def close(self):
        self.db.close()