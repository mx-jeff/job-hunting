from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

global driver

class Infojobs:
    global driver

    def __init__(self):

        self.options = Options()
        self.options.add_argument('--disable-notifications')
        self.options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome("C:/Selenium/chromedriver.exe", options=self.options)
        self.driver.get('http://www.infojobs.com.br')
        self.driver.implicitly_wait(10)

    def login(self):

        self.loginForm = self.driver.find_element_by_xpath('//*[@id="ctl00_cAccess_aLogin"]')
        self.loginForm.click()

        self.inputForm = self.driver.find_element_by_xpath('//*[@id="ctl00_cAccess_txtLogin"]')
        self.inputForm.send_keys('mx.jeferson.10@hotmail.com')

        self.passwordForm = self.driver.find_element_by_xpath('//*[@id="ctl00_cAccess_txtPwd"]')
        self.passwordForm.send_keys('saopaulo1')

        self.submitButton = self.driver.find_element_by_xpath('//*[@id="ctl00_cAccess_btnLogin"]')
        self.submitButton.click()

    def handleJobs(self):
        self.searchJob = self.driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[4]/div[6]/section[1]/div/div/ol/li[1]/input')
        self.searchJob.send_keys('python')
        self.searchJob.submit()


def main():
    jobs = Infojobs()
    jobs.login()
    jobs.handleJobs()


if __name__ == "__main__":
    main()