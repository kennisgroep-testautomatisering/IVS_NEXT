from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        

class MainPage(BasePage):
    def login(self, username, password):
        WAIT = 30
        wait = WebDriverWait(self.driver, WAIT)
        logging.info("Going to login")
        locator_login = (By.CSS_SELECTOR, "#login-button")
        elem = wait.until(EC.presence_of_element_located(locator_login))
        elem.click()
        locator_username = (By.CSS_SELECTOR, ".text[name='user.name']")
        elem = wait.until(EC.presence_of_element_located(locator_username))
        elem.send_keys(username)
        locator_password = (By.CSS_SELECTOR, ".text[type='password']")
        elem = wait.until(EC.presence_of_element_located(locator_password))
        elem.send_keys(password)
        locator_login_button = (By.CSS_SELECTOR, ".submit")
        elem = wait.until(EC.presence_of_element_located(locator_login_button))
        elem.click()
        
    def logout(self):
        WAIT = 30
        wait = WebDriverWait(self.driver, WAIT)
        logging.info("Going to logout")
        locator_person = (By.CSS_SELECTOR, "#current-username")
        elem = wait.until(EC.presence_of_element_located(locator_person))
        elem.click()
        locator_logout = (By.CSS_SELECTOR,".dropdown-menu-right #logout-button")
        elem = wait.until(EC.element_to_be_clickable(locator_logout))
        time.sleep(5)
        #elem = wait.until(EC.presence_of_element_located(locator_logout))
        elem.click()
