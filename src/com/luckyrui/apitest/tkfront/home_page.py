'''
Created on 2016-07-31 09:51:35

@author: chenrui
'''

from Tkinter import *
# from com.luckyrui.apitest.tkfront.menu import ATMenu

class ATHome(Frame):
    '''
    Api test IDE home Page
    '''


    def __init__(self, master = None):
        '''
        Init Frame
        '''
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        
        self.helloLabel = Label(self,text = "Hello,word!")
        self.helloLabel.pack()
        self.quitButton = Button(self,text="Quit",command = self.quit)
        self.quitButton.pack()