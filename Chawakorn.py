from selenium import webdriver
import selenium
import random
import time

class Bot:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def Start(self):
        selenium_ = selenium.webdriver.Chrome()
        selenium_.get(self.url)
        time.sleep(.5)
        self.driver = selenium_
    
    def send_Click(self, xpath):
        self.driver.find_element('xpath', xpath).click()

    def send_Random_Fill_Form(self, arr_xpath):
        self.driver.find_element('xpath', arr_xpath[random.randint(0, len(arr_xpath) - 1)]).click()
        
    def send_Fill_Form(self, xpath, Text):
        self.driver.find_element('xpath', xpath).send_keys(Text)
        
    def close(self):
        time.sleep(.3)
        self.driver.quit()