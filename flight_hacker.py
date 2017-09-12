import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Bot:

    def __init__(self):
        self.browser = webdriver.Firefox(executable_path='./geckodriver')
        # self.browser = webdriver.Chrome('./chromedriver')
        self.run()

    def run(self):
        try:
            self.search()
            self.findPrices()
        except Exception as ex:
            print(ex)
            self.browser.quit()

    def search(self):
        self.browser.get('https://www.google.com/flights/');
        departure_city = "COU"
        destination_city = "HND"
        departure_take_off_boxes = self.browser.execute_script(
            "return document.getElementsByClassName('EIGTDNC-Kb-f EIGTDNC-Kb-b')")
        print(departure_take_off_boxes[0].get_attribute('outerHTML'))
        print(departure_take_off_boxes[1].get_attribute('outerHTML'))
        departure_take_off_boxes[0].send_keys(departure_city)
        departure_take_off_boxes[0].send_keys(Keys.RETURN)
        time.sleep(1)
        departure_take_off_boxes[1].send_keys(destination_city)
        departure_take_off_boxes[1].send_keys(Keys.RETURN)
        time.sleep(1)





Bot()
