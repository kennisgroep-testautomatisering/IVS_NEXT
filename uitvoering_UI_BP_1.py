from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        
class uitvoering_UI_BP_1(BasePage):
    def new_brugplanning(self, boot, eni_nummer):
        WAIT = 30
        wait = WebDriverWait(self.driver, WAIT)
        locator_tab_rechts = (By.CSS_SELECTOR,'#tabs-rechts')
        elem = wait.until(EC.presence_of_element_located(locator_tab_rechts))
        boten = []
        boten = elem.find_elements_by_css_selector('.vaartuig-identifier')
        for boot in boten:
            if (boot.text==eni_nummer) :
                logging.info("De juiste boot is gevonden")
                break
            
        locator_add_brug_planning = (By.CSS_SELECTOR,'.add-button[type="button"]')
        elem = wait.until(EC.presence_of_element_located(locator_add_brug_planning))
        elem.click()
        
    def sleur_en_pleur(self,boot,eni_nummer):
        WAIT = 30
        wait = WebDriverWait(self.driver, WAIT)
        driver = self.driver
        locator_planning_window = (By.CSS_SELECTOR,'.actuele-planning#brugplanning-0')
        planning = wait.until(EC.presence_of_element_located(locator_planning_window))
        brugplanning_rechts = planning.find_element_by_css_selector(".brugplanning-rechts .vaartuigen")
        locator_tab_rechts = (By.CSS_SELECTOR,'#tabs-rechts')
        elem = wait.until(EC.presence_of_element_located(locator_tab_rechts))
        boten = []
        boten = elem.find_elements_by_css_selector('.vaartuig-rows')
        for boot in boten:
            identifier = boot.find_element_by_css_selector('.vaartuig-identifier')
            if (identifier.text==eni_nummer):
                dest_height = brugplanning_rechts.size['height']/2
                dest_width = brugplanning_rechts.size['width']/2
                xoffset = brugplanning_rechts.location['x'] + dest_height
                yoffset = brugplanning_rechts.location['y'] + dest_width
                print(xoffset)
                print(yoffset)
                #ActionChains(driver).click_and_hold(boot).move_to_element(brugplanning_rechts).release(brugplanning_rechts).perform()
                #ActionChains(driver).drag_and_drop(boot, brugplanning_rechts).perform()
                #ActionChains(driver).drag_and_drop_by_offset(boot, xoffset, yoffset)
                ActionChains(driver).move_to_element(boot).perform()
                ActionChains(driver).click_and_hold(boot)
                ActionChains(driver).move_to_element(brugplanning_rechts).perform()
                ActionChains(driver).release(brugplanning_rechts)
                #Drag en Drop werkt nog niet. Nu maar uitloggen dan
                break
                
        
        
        
        
        
        
        
        
        