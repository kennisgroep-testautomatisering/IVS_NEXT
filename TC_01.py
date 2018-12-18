import datetime
import unittest
import logging
import configparser
import page
import voorbereiding_UI_BP_1
import uitvoering_UI_BP_1
import os


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.firefox.webdriver import FirefoxProfile


class TestCase_01(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read("/var/ini/init.ini")
        #self.config.read("C:/IVS_Next_KTV/ini/init.ini")
        
        
        logfile = os.environ["logfile"] 
        logging.basicConfig(level=logging.INFO, filename = '../logs/'+ logfile)
        logging.info("Setting up Driver")
        
        #binary = FirefoxBinary('/usr/local/firefox/firefox')
        
        chromeOptions = Options()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument("--window-size=1920,1080")
        chromeOptions.add_argument('--disable-dev-shm-usage')
        
        self.driver = webdriver.Chrome(r"/usr/local/bin/chromedriver",chrome_options=chromeOptions)
        #self.driver = webdriver.Chrome(r"C:/Selenium_Jar_MR/anders/chromedriver.exe",chrome_options=chromeOptions)

#         ffProfile = FirefoxProfile()
#         ffProfile.accept_untrusted_certs = True
#         ffProfile.accept_insecure_certs = True
#         ffProfile.assume_untrusted_cert_issuer = True
#         self.driver = webdriver.Firefox(firefox_profile=ffProfile)

        
        logging.info("Setting Driver Settings")
        self.driver.maximize_window()
        link = "https://acceptatie2.vos.intranet.rijkswaterstaat.nl/ivs-gui-frontend/#/mededelingen"
        driver = self.driver
        driver.get(link)
    
    def voorbereiding_start(self):
        main_page = page.MainPage(self.driver)
        data = self.config['INITdata']
        username = data['loginnaam']
        password = data['password']
        main_page.login(username, password)
        ivs_page = voorbereiding_UI_BP_1.IVSPage(self.driver)
        ivs_page.navigate()
        boot = data['test_boot']
        eni_nummer = data['eni_nummer']
        ivs_page.voorbereiding_brugplanning(boot,eni_nummer)
        
    def uitvoering_start(self):
        data = self.config['INITdata']
        boot = data['test_boot']
        eni_nummer = data['eni_nummer']
        ivs_page = uitvoering_UI_BP_1.uitvoering_UI_BP_1(self.driver)
        ivs_page.new_brugplanning(boot,eni_nummer)
        ivs_page.sleur_en_pleur(boot,eni_nummer)
        main_page = page.MainPage(self.driver)
        main_page.logout()
        
    def test_uc01(self):
        self.voorbereiding_start()
        self.uitvoering_start()
        
    def tearDown(self):
        #self.driver.close()
        pass
        

if __name__ == '__main__':
    logfile = datetime.datetime.today().strftime('%Y%m%d%H%M%S%f') +'.log'
    os.environ["logfile"] = logfile
    log_file = 'log_file.txt'
    f = open(log_file, "a")
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner,exit=False)
    f.close()
    f = open(log_file, "r")
    file = open('../logs/'+logfile, "a")
    file.write('\n')
    file.write (f.read())
    file.close()
    f.close()
    os.remove(log_file)
