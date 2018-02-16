'''
Created on Feb 12, 2018

@author: King
'''
class Browser(object):

    def __init__(self, driver):
        self.driver = driver;
        
    def Open(self):
        self.driver.get("http://192.168.2.17:5000")
