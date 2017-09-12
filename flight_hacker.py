import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bot:

    def __init__(self):
        self.browser = webdriver.Firefox(executable_path='./geckodriver')
        # self.browser = webdriver.Chrome('./chromedriver')
        self.prices = []
        self.Run()

    def Run(self):
        try:
            self.Search()
            self.FindPrices()
            self.SendText()
        except Exception as ex:
            print(ex)
            self.browser.quit()

    def Search(self):
        self.browser.get('https://www.google.com/flights/');
        departure_city = "COU"
        destination_city = "HND"
        departure_take_off_boxes = self.browser.execute_script(
            "return document.querySelectorAll('.EIGTDNC-Kb-f.EIGTDNC-Kb-b')")
        print(departure_take_off_boxes[0].get_attribute('outerHTML'))
        print(departure_take_off_boxes[1].get_attribute('outerHTML'))
        departure_take_off_boxes[0].send_keys(departure_city)
        departure_take_off_boxes[0].send_keys(Keys.RETURN)
        time.sleep(1)
        self.browser.implicitly_wait(10)
        departure_take_off_boxes[1].send_keys(destination_city)
        departure_take_off_boxes[1].send_keys(Keys.RETURN)
        time.sleep(1)

    def FindPrices(self):
        self.browser.implicitly_wait(10) 
        self.prices = self.browser.execute_script(
            "return document.querySelectorAll('.EIGTDNC-d-bc')")
        print(self.prices)

    def SendText(self):
        print('text will go here')

Bot()
