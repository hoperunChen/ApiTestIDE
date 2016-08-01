'''
Created on 2016-08-01 21:40:06

@author: chenrui
'''
from com.luckyrui.apitest.utils.conf_reader_util import ConfReader
import sqlite3

# get db address
confReader = ConfReader()
dbaddr = confReader.get('addr', 'db')

def getConnection():
    '''get connection Object
    '''
    return sqlite3.connect(dbaddr)

def executeQuery(conn, sql, params):
    '''execute Query 
    '''
    if conn == None:
        raise Exception('conn is null')
    if sql == None:
        raise Exception('sql is null')
    cursor = conn.cursor()
    if params == None:
        cursor.execute(sql)
    else :
        cursor.execute(sql, params)
    values = cursor.fetchall()
    col_name = [t[0] for t in cursor.description] 
    cursor.close()
    #build a return table
    dataset = []
    for value in values:
        row = {}
        for i in range(len(value)):
            row[col_name[i]] = value[i]
        dataset.append(row)
    return dataset
