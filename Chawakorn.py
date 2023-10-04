from selenium import webdriver
import selenium
import random
import time

class Bot:
    def __init__(self, url):
        self.url = url
        self.driver = None
        self.score = 0

    def Start(self):
        selenium_option = webdriver.ChromeOptions()
        selenium_option.add_argument('--log-level=3')
        selenium_ = webdriver.Chrome(options=selenium_option)
        selenium_.get(self.url)
        time.sleep(.5)
        self.driver = selenium_
    
    def send_Click(self, xpath):
        self.driver.find_element('xpath', xpath).click()

    def send_Random_Click(self, arr_xpath):
        number = random.randint(0, len(arr_xpath) - 1)
        self.send_Click(arr_xpath[number])

    def send_Fill_Form(self, xpath, Text):
        self.driver.find_element('xpath', xpath).send_keys(Text)
    
    def close(self):
        time.sleep(.3)
        self.driver.quit()