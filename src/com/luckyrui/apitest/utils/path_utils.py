# -*- coding: UTF-8 -*-     
'''
Created on 2016-1-27

@author: cr
'''

import os,sys

'''获取工程的绝对路径
前提是工程目录是:
    project
        -src
        -resource
'''
def getProjectName():
    absPath=os.path.abspath(sys.argv[0]) 
    absPath=os.path.dirname(absPath)+"/"
    absPath = absPath[0:absPath.find('/src/')]
    return absPath

'''获取工程的resource绝对路径
前提是工程目录是:
    project
        -src
        -resource
'''
def getConfPath():
    absPath = getProjectName()
    return absPath+'/resources/'

'''获取工程的src绝对路径
前提是工程目录是:
    project
        -src
        -resource
'''
def getSrcPath():
    absPath = getProjectName()
    return absPath+'/src/'
