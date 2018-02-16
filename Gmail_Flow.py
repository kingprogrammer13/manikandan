'''
Created on Feb 13, 2018

@author: King
'''
import time
import Gmail_Path

class Gmail_Flow(object):
    
    def __init__(self, driver):
        self.driver=driver
        
    def Gmail(self):
        driver=self.driver
        driver.get("http://www.gmail.com")
        driver.find_element_by_xpath(Gmail_Path.Gmail_ID).send_keys("tech.cod.mk13@gmail.com")
        driver.find_element_by_xpath(Gmail_Path.Gmail_next).click()
        time.sleep(3)
        driver.find_element_by_xpath(Gmail_Path.GPass).send_keys("123456789theKINGofPRINCY987654321")
        driver.find_element_by_xpath(Gmail_Path.GPass_next).click()
        driver.find_element_by_xpath(Gmail_Path.E_Search).clear()
        time.sleep(5)
        driver.find_element_by_xpath(Gmail_Path.E_Search).sendkeys("OpenWorld new Password")
        driver.find_element_by_xpath(Gmail_Path.E_S_Click).click()
        driver.find_element_by_class_name(Gmail_Path.E_IN_LINK).click()   