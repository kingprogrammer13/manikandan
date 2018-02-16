'''
Created on Feb 12, 2018

@author: King
'''
from selenium import webdriver
import Browser
import Login_Page
import Gmail_Flow

class login(object):
    
    def Main(self):
        self.driver = webdriver.Chrome()
        DVR=Browser.Browser(self.driver)           
        DVR.Open()                               
    def Login(self):
        LOG=Login_Page.Login_Page(self.driver)
        LOG.Login()
    def Gmail(self):
        Mail=Gmail_Flow.Gmail_Flow(self.driver)
        Mail.Gmail()    
    
def main():
    OBJ=login()
    OBJ.Main()
    OBJ.Login()
    OBJ.Gmail()
    
if __name__=="__main__":
    main()