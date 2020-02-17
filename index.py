from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class Infojobs:
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

    def searchList(self, jobType):
        self.searchJob = self.driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[3]/div[6]/section[1]/div/div/ol/li[1]/input')
        self.searchJob.send_keys(str(jobType))
        self.searchJob.send_keys(Keys.ENTER)

    def searchOptions(self):
        self.cityOptionSaoPaulo = self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_cFacetLocation3_rptFacet_ctl01_chkItem"]').click()
        #self.cltOption = self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_cFacetContractWorkType_rptFacet_ctl01_chkItem"]').click()
        #self.jobOption = self.driver.find_element_by_xpath('')

    def getJob(self):
        self.driver.implicitly_wait(5)
        self.jobsContainer = self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_resultsGrid"]')
        self.sourceCode = self.jobsContainer.get_attribute('outerHTML')
        return self.sourceCode

    @staticmethod
    def saveHTML(html):
        with open('test.html', 'wb') as file:
            file.write(html.encode('utf-8'))

    def quitSearch(self):
        self.driver.quit()


def main():
    jobs = Infojobs()
    jobs.login()
    jobs.searchList('python')
    jobs.searchOptions()
    jobs.getJob()
    jobs.saveHTML(jobs.getJob())
    jobs.quitSearch()


if __name__ == "__main__":
    main()
