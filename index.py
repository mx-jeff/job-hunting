from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


class Infojobs:
    jobsLink = []

    def __init__(self):

        self.options = Options()
        self.options.add_argument('--disable-notifications')
        #self.options.add_argument('--headless')
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
        self.searchJob = self.driver.find_element_by_xpath('/html/body/form/div[3]/div[6]/section[1]/div/div/ol/li[1]/input')
        self.searchJob.send_keys(str(jobType))
        self.searchJob.send_keys(Keys.ENTER)

    def searchOptions(self):
        try:
            self.cityOptionSaoPaulo = self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_cFacetLocation3_rptFacet_ctl01_chkItem"]').click()
            self.cltOption = self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_cFacetContractWorkType_rptFacet_ctl01_chkItem"]').click()
            #self.jobOption = self.driver.find_element_by_xpath('')
        except:
            sleep(10)
            self.cltOption = self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_cFacetContractWorkType_rptFacet_ctl01_chkItem"]').click()

        sleep(10)

    def getJob(self):
        try:
            sleep(5)
            self.jobsContainer = self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_resultsGrid"]')
            #self.jobTarget = self.driver.find_element_by_xpath('/html/body/form/section/div/div[1]/section[2]/div[2]/div[3]/div[2]/a').click()
            self.links = self.jobsContainer.find_elements_by_tag_name('a')
            for link in self.links:
                self.jobsLink.append(link.get_attribute('href').replace(',',''))

            for target in self.jobsLink:
                self.driver.get(target)
                sleep(5)
                self.driver.back()
            
        except:
            pass
            raise

    def subscribeJob(self, link):
        driver = self.driver
        
        driver.get(link)
        sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_cHeader_lnkCandidatar"]').click()
            sleep(5)
            driver.back()
            sleep(5)
            driver.back()
        except:
            raise

    @staticmethod
    def saveHTML(html):
        with open('test.html', 'wb') as file:
            file.write(html.encode('utf-8'))

    @staticmethod
    def saveFile(data):
        with open('data.txt', 'w') as file:
            file.write("\n".join(str(item) for item in data))

    def quitSearch(self):
        self.driver.quit()


def main():
    jobs = Infojobs()
    jobs.login()
    jobs.searchList('jovem aprendiz')
    jobs.searchOptions()
    jobs.getJob()
    #Infojobs.saveFile(Infojobs.jobsLink)
    jobs.quitSearch()
    



if __name__ == "__main__":
    main()
