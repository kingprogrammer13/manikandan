'''
Created on Feb 12, 2018

@author: King
'''
import Login_Path
class Login_Page(object):
    
    def __init__(self, driver):
        self.driver=driver;
        
    def Login(self):
        driver=self.driver
        driver.find_element_by_xpath(Login_Path.username).send_keys('mani@1011')
        driver.find_element_by_xpath(Login_Path.password).send_keys('Mani@1011')
        driver.find_element_by_xpath(Login_Path.L_login).click()
