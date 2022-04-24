from selenium import webdriver
import time


class Selenium:

    def __init__(self):

        self.driver = webdriver.Chrome()

    def authorization(self, login, password):

        self.driver.get('https://opensource-demo.orangehrmlive.com')
        time.sleep(3)
        login_element = self.driver.find_element_by_id("txtUsername")
        password_element = self.driver.find_element_by_id("txtPassword")
        login_element.send_keys(login)
        password_element.send_keys(password)
        login_button = self.driver.find_element_by_id("btnLogin")
        login_button.click()
        message = self.driver.find_element_by_id("spanMessage").text
        return message

