import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bot:

    def __init__(self):
        # self.browser = webdriver.Firefox(executable_path='./geckodriver')
        self.browser = webdriver.Chrome('./chromedriver')
        self.departure_airport = "COU"
        self.destination_airport = "HND"
        self.departure_day = "March 1"
        self.return_day = "March 10"
        self.prices = []
        self.Run()

    def Run(self):
        try:
            self.SetFlight()
            # self.SetDates()
            # self.FindPrices()
            # self.SendText()
            # time.sleep(10)
            # self.browser.quit()

            
        except Exception as ex:
            print(ex)
            self.browser.quit()

    def SetFlight(self):
        self.browser.get('https://www.kayak.com/')
        self.browser.implicitly_wait(20)
        departure_take_off_boxes = self.browser.execute_script(
            "return document.querySelectorAll('.gws-flights-form__input-target')")
        print(departure_input)
        # departure_input.send_keys(self.departure_airport)

        time.sleep(1)
        # # departure_take_off_boxes[1].send_keys(self.destination_airport)
        # # departure_take_off_boxes[1].send_keys(Keys.RETURN)
        # time.sleep(1)

    def SetDates(self):
        departure_take_off_dates = self.browser.execute_script(
            "return document.querySelectorAll('.EIGTDNC-G-s input')")
        print(departure_take_off_dates[0].get_attribute('outerHTML'))
        print(departure_take_off_dates[1].get_attribute('outerHTML'))
        departure_take_off_dates[0].click()
        departure_take_off_dates[0].send_keys(self.departure_day)
        departure_take_off_dates[0].send_keys(Keys.RETURN)
        departure_take_off_dates[1].send_keys(self.return_day)
        departure_take_off_dates[1].send_keys(Keys.RETURN)

    def FindPrices(self):
        self.browser.implicitly_wait(10) 
        self.prices = self.browser.execute_script(
            "return document.querySelectorAll('.EIGTDNC-d-bc')")
        # print(self.prices)


    def SendText(self):
        print('text will go here')

Bot()
