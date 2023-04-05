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

    def send_Random_Fill_Form(self, arr_xpath, append_score):
        number = random.randint(0, len(arr_xpath) - 1)
        self.driver.find_element('xpath', arr_xpath[number]).click()
        if(append_score):
            score = self.score
            self.score = score + number

    def send_Fill_Form(self, xpath, Text):
        self.driver.find_element('xpath', xpath).send_keys(Text)
        
    def get_Level(self):
        score = self.score
        if(score > 45):
            return 'อาการซึมเศร้าระดับรุนแรงมาก'
        elif(score > 31,40):
            return 'อาการซึมเศร้าระดับรุนแรงค่อนข้างมาก'
        elif(score > 21,30):
            return 'อาการซึมเศร้าในระดับปานกลาง'
        elif(score > 16,20):
            return 'อาการซึมเศร้าในระดับเล็กน้อย'
        else:
            return 'อาการซึมเศร้าหรือมีอาการของโรคในระดับน้อยมาก'
        
    def close(self):
        time.sleep(.3)
        self.driver.quit()