'''
Script to read browser using selenium driver. 

You must have the drivers installed. 
'''
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Browser():

    def __init__(self, url, browser):
        if url == "" or url is None:
            raise Exception('No URL called')
        self.url = url
        if browser == "ff":
            self.ff_browse()
        elif browser == "chrome":
            self.chrome_browse()
        else:
            raise Exception('No driver given')

    def ff_browse(self):
        '''
            Method to run Firefox headless browser
        '''
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

        reportname = "./reports/{}_ff_report.json".format(self.url.replace("https://warwick.ac.uk/fac/cross_fac/", "").replace('/', "_"))
        self._browse(driver, reportname)

    def chrome_browse (self):
        '''
            Method to run Chrome headless browser
        '''
        options = Options()
        options.add_argument("-headless")
        driver = webdriver.Chrome(options=options)
        reportname = "./reports/{}_chrome_report.json".format(self.url.replace("https://warwick.ac.uk/fac/cross_fac/", "").replace('/', "_"))
        self._browse(driver, reportname)

    def _browse(self, driver, report_name):
        '''
            Method to run the browser tests

            :param driver - selenium driver to run
            :param reportname - name for the report
        '''

        driver.get(self.url)
        driver.implicitly_wait(10)

        axe_script = open('./axe.min.js', 'r')
        
        driver.execute_script(axe_script.read())

        axe_script.close()

        result = driver.execute_async_script('var callback = arguments[arguments.length - 1];'
                                            'axe.run().then(results => callback(results))')
        file = open(report_name, "w")

        file.write(json.dumps(eval(str(result))))

        file.close()

        driver.quit()
