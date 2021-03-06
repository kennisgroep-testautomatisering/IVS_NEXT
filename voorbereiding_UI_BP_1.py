from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import re


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        
class IVSPage(BasePage):
    def navigate(self):
        WAIT = 30
        wait = WebDriverWait(self.driver, WAIT)
        logging.info("Going to Sas van Gent Brug")
        locator_login = (By.LINK_TEXT, "Sas van Gent, brug")
        elem = wait.until(EC.presence_of_element_located(locator_login))
        elem.click()
        
    def voorbereiding_brugplanning(self, boot, eni_nummer):
        WAIT = 30
        wait = WebDriverWait(self.driver, WAIT)
        driver = self.driver
        logging.info("Zoek boot KTV-KAT03")
        locator_zoeken = (By.CSS_SELECTOR, "#vaartuig-search-input")
        elem = wait.until(EC.presence_of_element_located(locator_zoeken))
        elem.send_keys(boot)
        
        locator_window = (By.TAG_NAME, "ivs-overlay-window")
        window = wait.until(EC.presence_of_element_located(locator_window))
        
        locator_sub_venster = (By.CSS_SELECTOR, ".vaartuig-search-result-container")
        venster = wait.until(EC.presence_of_element_located(locator_sub_venster))
        
        boten = []
        boten = venster.find_elements_by_css_selector('.vaartuig-identifier')
        for boot in boten:
            if (boot.text == eni_nummer):
                boot.click()
                break
                
        locator_boot = (By.CSS_SELECTOR,"[type='button'][aria-haspopup='true']")
        elem = wait.until(EC.presence_of_element_located(locator_boot))
        
        logging.info("Zet de status van de boot naar Actueel")
        
        locator_drop_down = (By.CSS_SELECTOR,".controle-and-acties [type='button'][aria-haspopup='true']")
        drop_down = wait.until(EC.presence_of_element_located(locator_drop_down))
        if (drop_down!='Actueel'):
            logging.info("De status van de boot is niet Actueel")
            drop_down.click()
            locator_menu = (By.CSS_SELECTOR, '[aria-labelledby="vaarreisSegment-status"]')
            elem = wait.until(EC.presence_of_element_located(locator_menu))
            options = []
            options = elem.find_elements_by_css_selector('.ng-star-inserted')
            for option in options:
                #print (option.text)
                if(option.text == 'Actueel'): 
                    option.click()
                    locator_publiceer = (By.CSS_SELECTOR,'#publiceer-reis-button')
                    elem = wait.until(EC.presence_of_element_located(locator_publiceer))
                    logging.info("De nieuwe status wordt gepubliceerd")
                    elem.click()
                    #Hier krijgen we meuk
                    
                    break
           
        locator_positie = (By.CSS_SELECTOR,'#invoeren-positie')
        elem = wait.until(EC.presence_of_element_located(locator_positie))
        logging.info("De positie van de boot veranderen")
        elem.click() 
        locator_submenu = (By.CSS_SELECTOR,"[aria-labelledby='vaarreis-muteren-positie-vaarrichting']")
        elem = wait.until(EC.presence_of_element_located(locator_submenu))
        locator_afvarend = (By.CSS_SELECTOR,'.dropdown-item[translate="VTS_GEBIEDSLIJST.AFVAREND"]')
        elem = wait.until(EC.presence_of_element_located(locator_afvarend)) 
        elem.click()
        locator_publiceren = (By.CSS_SELECTOR,'.justify-content-between')
        elem = wait.until(EC.presence_of_element_located(locator_publiceren))
        elem.click()
        locator_kruisje = (By.CSS_SELECTOR,".btn-delete[container='body']")
        elem = wait.until(EC.presence_of_element_located(locator_kruisje))
        elem.click()
        locator_window_title = (By.CSS_SELECTOR, '.text-uppercase[translate="BRUGPLANNING.TITLE"]')
        elem = wait.until(EC.presence_of_element_located(locator_window_title))
        locator_ververs = (By.CSS_SELECTOR,'.sector-click-to-refresh')
        logging.info("Hoofdscherm verversen")
        elem = wait.until(EC.presence_of_element_located(locator_ververs))
        elem.click()

