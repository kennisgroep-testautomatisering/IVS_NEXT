from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
import sys
import time
import os

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        
class uitvoering_UI_BP_2(BasePage):
    def new_brugplanning(self, schip,eni_nummer,schip2,eni_nummer2):
        WAIT = int(os.environ["web_wait"])
        wait = WebDriverWait(self.driver, WAIT)
        locator_tab_rechts = (By.CSS_SELECTOR,'#tabs-rechts')
        elem = wait.until(EC.presence_of_element_located(locator_tab_rechts))
        juiste_schip = False
        for i in [0,1]:
            if (i==0):
                schip = schip
                eni_nummer = eni_nummer
            elif (i==1):
                schip = schip2
                eni_nummer = eni_nummer2
        
            for i in range(WAIT):
                schepen = []
                schepen = elem.find_elements_by_css_selector('.vaartuig-identifier')
                for boot in schepen:
                    if (boot.text==eni_nummer) :
                        juiste_schip = True
                        break
                if(juiste_schip):
                    break
                time.sleep(0.1)
            
            if (juiste_schip):
                logging.info("Het juiste schip is gevonden "+str(schip))
            elif(not juiste_schip):
                logging.info("Het juiste schip is NIET gevonden "+str(schip))
                sys.exit(1)

        locator_add_brug_planning = (By.CSS_SELECTOR,'.add-button[type="button"]')
        elem = wait.until(EC.presence_of_element_located(locator_add_brug_planning))
        elem.click()
        
    def sleur_en_pleur(self,schip,eni_nummer,schip2,eni_nummer2):
        WAIT = int(os.environ["web_wait"])
        wait = WebDriverWait(self.driver, WAIT)
        driver = self.driver
        for i in [0,1]:
            if (i==0):
                schip = schip
                eni_nummer = eni_nummer
            elif (i==1):
                schip = schip2
                eni_nummer = eni_nummer2
        
            locator_planning_window = (By.CSS_SELECTOR,'.actuele-planning#brugplanning-0')
            planning = wait.until(EC.presence_of_element_located(locator_planning_window))
            brugplanning_rechts = planning.find_element_by_css_selector(".brugplanning-rechts .vaartuigen")
            locator_tab_rechts = (By.CSS_SELECTOR,'#tabs-rechts')
            elem = wait.until(EC.presence_of_element_located(locator_tab_rechts))
            schepen = []
            schepen = elem.find_elements_by_css_selector('.vaartuig-card')
            for boot in schepen:
                identifier = boot.find_element_by_css_selector('.vaartuig-identifier')
                if (identifier.text==eni_nummer):
                    print(eni_nummer)
                    JS_HTML5_DND = 'function e(e,t,n,i){var r=a.createEvent("DragEvent");r.initMouseEvent(t,!0,!0,o,0,0,0,c,g,!1,!1,!1,!1,0,null),Object.defineProperty(r,"dataTransfer",{get:function(){return d}}),e.dispatchEvent(r),o.setTimeout(i,n)}var t=arguments[0],n=arguments[1],i=arguments[2]||0,r=arguments[3]||0;if(!t.draggable)throw new Error("Source element is not draggable.");var a=t.ownerDocument,o=a.defaultView,l=t.getBoundingClientRect(),u=n?n.getBoundingClientRect():l,c=l.left+(l.width>>1),g=l.top+(l.height>>1),s=u.left+(u.width>>1)+i,f=u.top+(u.height>>1)+r,d=Object.create(Object.prototype,{_items:{value:{}},effectAllowed:{value:"all",writable:!0},dropEffect:{value:"move",writable:!0},files:{get:function(){return this._items.Files}},types:{get:function(){return Object.keys(this._items)}},setData:{value:function(e,t){this._items[e]=t}},getData:{value:function(e){return this._items[e]}},clearData:{value:function(e){delete this._items[e]}},setDragImage:{value:function(e){}}});if(n=a.elementFromPoint(s,f),!n)throw new Error("The target element is not interactable and need to be scrolled into the view.");u=n.getBoundingClientRect(),e(t,"dragstart",101,function(){var i=n.getBoundingClientRect();c=i.left+s-u.left,g=i.top+f-u.top,e(n,"dragenter",1,function(){e(n,"dragover",101,function(){n=a.elementFromPoint(c,g),e(n,"drop",1,function(){e(t,"dragend",1,callback)})})})})'
                    e1 = boot
                    e2 = brugplanning_rechts
                    driver.execute_script(JS_HTML5_DND, e1, e2)
                    logging.info("Het schip is gesleept "+str(schip))
                    time.sleep(0.1)
                    break
               
    def check(self,schip,eni_nummer,schip2,eni_nummer2):
        WAIT = int(os.environ["web_wait"])
        wait = WebDriverWait(self.driver, WAIT)
        driver = self.driver
        
        for i in [0,1]:
            if (i==0):
                schip = schip
                eni_nummer = eni_nummer
            elif (i==1):
                schip = schip2
                eni_nummer = eni_nummer2
        
        #Check: schip staat in de lijst ingedeeld 
            locator_ingedeeld = (By.CSS_SELECTOR, "#tabs-rechts .tab-header-ingedeeld .nav-link")
            elem = wait.until(EC.presence_of_element_located(locator_ingedeeld))
            elem.click()
            locator_tab_rechts = (By.CSS_SELECTOR,'#tabs-rechts')
            elem = wait.until(EC.presence_of_element_located(locator_tab_rechts))
            juiste_schip = False
            
            for i in range(WAIT):
                schepen = []
                schepen = elem.find_elements_by_css_selector('.vaartuig-card')
                if (len(schepen)>0):
                    for boot in schepen:
                        identifier = boot.find_element_by_css_selector('.vaartuig-identifier')
                        if (identifier.text==eni_nummer):
                            juiste_schip = True
                            break
                if (juiste_schip):
                    break
                time.sleep(0.1)    
                
            if (juiste_schip):
                logging.info("Het juiste schip is ingedeeld "+str(schip))
            elif(not juiste_schip):
                logging.info("Het juiste schip is NIET ingedeeld "+str(schip))
                sys.exit(1)
        
         
            #Check: Schip staat niet meer op de aanbodslijst 
            locator_aanbod = (By.CSS_SELECTOR, "#tabs-rechts .tab-header-aanbod .nav-link")
            elem = wait.until(EC.presence_of_element_located(locator_aanbod))
            elem.click()
            
            locator_tab_rechts = (By.CSS_SELECTOR,'#tabs-rechts')
            elem = wait.until(EC.presence_of_element_located(locator_tab_rechts))
            juiste_schip = False
    
            for i in range(WAIT):
                schepen = []
                schepen = elem.find_elements_by_css_selector('.vaartuig-card')
                if (len(schepen)>0):
                    for boot in schepen:
                        identifier = boot.find_element_by_css_selector('.vaartuig-identifier')
                        if (identifier.text==eni_nummer):
                            juiste_schip = True
                            break
                if(not juiste_schip):
                    break
                time.sleep(0.1)
                
            if (juiste_schip):
                logging.info("Het schip staat in de aanbodlijst "+schip)
                sys.exit(1)
            elif(not juiste_schip):
                logging.info("Het schip staat NIET in de aanbodlijst "+schip)                

        
            #Check: Schip staat in de brugplanning 
            locator_planning_window = (By.CSS_SELECTOR,'.actuele-planning#brugplanning-0')
            planning = wait.until(EC.presence_of_element_located(locator_planning_window))
            brugplanning_rechts = driver.find_element_by_css_selector(".actuele-planning#brugplanning-0 .brugplanning-rechts .vaartuigen")
            juiste_schip = False
            
            for i in range(WAIT):
                schepen = []
                schepen = brugplanning_rechts.find_elements_by_css_selector('.vaartuig-card')
                if (len(schepen)>0):
                    for boot in schepen:
                        identifier = boot.find_element_by_css_selector('.vaartuig-naam .text-truncate')
                        if (identifier.text==schip):
                            juiste_schip = True
                            break
                if(juiste_schip):
                    break
                time.sleep(0.1)
                
            if (juiste_schip):
                logging.info("Het schip staat in de brugplanning "+schip)
    
            elif(not juiste_schip):
                logging.info("Het schip staat NIET in de brugplanning "+schip)
                sys.exit(1)
        
    def uitvoeren_brugplanning(self,schip,eni_nummer,schip2,eni_nummer2):
        
        WAIT = int(os.environ["web_wait"])
        wait = WebDriverWait(self.driver, WAIT)
        locator_brugplanning = (By.CSS_SELECTOR,".btn-openen")
        elem = wait.until(EC.element_to_be_clickable(locator_brugplanning))
        #time sleep ingebouwd voor de banners die verschijnen als reis niet actueel was.
        #time.sleep(3)
        elem.click()
        logging.info("Het stoplicht staat op groen")
        
        locator_brugplanning = (By.CSS_SELECTOR,".btn-sluiten")
        elem = wait.until(EC.element_to_be_clickable(locator_brugplanning))
        time.sleep(1)
        elem.click()
        logging.info("Het stoplicht staat op rood")
        
        locator_ja_knop = (By.CSS_SELECTOR,'#btn-do-update')
        elem = wait.until(EC.element_to_be_clickable(locator_ja_knop))
        time.sleep(0.1)
        elem.click()
        logging.info("Brugplanning gerealiseerd")
        
        for i in [0,1]:
            if (i==0):
                schip = schip
                eni_nummer = eni_nummer
            elif (i==1):
                schip = schip2
                eni_nummer = eni_nummer2
            #Check: Schip staat weer in de aanbodlijst (rechts)
            locator_tab_rechts = (By.CSS_SELECTOR,'#tabs-rechts')
            elem = wait.until(EC.presence_of_element_located(locator_tab_rechts))
            juiste_schip = False
            for i in range(WAIT):
                schepen = []
                schepen = elem.find_elements_by_css_selector('.vaartuig-card')
                if (len(schepen)>0):
                    for boot in schepen:
                        identifier = boot.find_element_by_css_selector('.vaartuig-identifier')
                        if (identifier.text==eni_nummer):
                            juiste_schip = True
                            break
                if(juiste_schip):
                    break
                time.sleep(0.1)
                
                
            if (juiste_schip):
                logging.info("Het schip staat in de aanbodlijst "+str(schip))
                
            elif(not juiste_schip):
                logging.info("Het schip staat NIET in de aanbodlijst "+str(schip))
                raise ValueError('Schip NIET gevonden '+schip)
            
            #Check: Brugplanning is verdwenen 
            locator_planning_window = (By.CSS_SELECTOR,'.actuele-planning#brugplanning-0')
            planning = wait.until(EC.presence_of_element_located(locator_planning_window))
            brugplanning_rechts = planning.find_element_by_css_selector(".brugplanning-rechts .vaartuigen")
            juiste_schip = False
            for i in range(WAIT):
                schepen = []
                schepen = brugplanning_rechts.find_elements_by_css_selector('.vaartuig-card')
                if (len(schepen)>0):
                    for boot in schepen:
                        identifier = boot.find_element_by_css_selector('.vaartuig-card .vaartuig-naam .text-truncate')
                        if (identifier.text==schip_naam):
                            juiste_schip = True
                            break
                if(not juiste_schip):
                    break
                time.sleep(0.1)
                
            if (juiste_schip):
                logging.info("Het schip staat in de brugplanning "+str(schip))
                raise ValueError('Schip staat nog in brugplanning '+str(schip))
    
            elif(not juiste_schip):
                logging.info("Het schip staat NIET in de brugplanning "+str(schip))
