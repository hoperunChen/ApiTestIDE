# -*- coding: UTF-8 -*-     
'''
Created on 2016-07-29 18:46:23
@author: chenrui
'''
import sys

from com.luckyrui.apitest.tkfront.home_page import ATHome
# from com.luckyrui.apitest.tkfront.menu import ATMenu
from com.luckyrui.apitest.utils import path_utils
from com.luckyrui.apitest.dbhandler import sqlite_handler as sqlite

print 'add path %s' %path_utils.getSrcPath()
sys.path.append(path_utils.getSrcPath())

if __name__ == '__main__':
    conn = sqlite.getConnection()
    values = sqlite.executeQuery(conn, 'select * from test_table', None)
    print values
    conn.close();
    for value in values:
        print value['name']
#     app = ATHome()
#     app.master.title("hello world")
#     app.master.config(menu = ATMenu(app.master))
#     app.mainloop()