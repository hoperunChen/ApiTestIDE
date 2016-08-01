# -*- coding: UTF-8 -*-     
'''
Created on 2016-07-29 18:46:23
@author: chenrui
'''
import sys

from com.luckyrui.apitest.tkfront.home_page import ATHome
from com.luckyrui.apitest.tkfront.menu import ATMenu
from com.luckyrui.apitest.utils import path_utils


print 'add path %s' %path_utils.getSrcPath()
sys.path.append(path_utils.getSrcPath())

if __name__ == '__main__':
    app = ATHome()
    app.master.title("hello world")
    app.master.config(menu = ATMenu(app.master))
    app.mainloop()