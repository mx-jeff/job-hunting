from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from credentails import user, password
from config import setSelenium


class Infojobs:
    appName = '[Job-hunting]'
    jobsLink = []

    def __init__(self):
        self.driver = setSelenium('http://www.infojobs.com.br')
        print(f'{self.appName} Iniciando...')

    def login(self):
        """
        Login to Infojobs, with credentials
        :return: None
        """
        print(f'{self.appName} Tentando logar...')
        self.loginForm = self.driver.find_element_by_xpath('//*[@id="ctl00_cAccess_aLogin"]')
        self.loginForm.click()

        self.inputForm = self.driver.find_element_by_xpath('//*[@id="ctl00_cAccess_txtLogin"]')
        self.inputForm.send_keys(user)

        self.passwordForm = self.driver.find_element_by_xpath('//*[@id="ctl00_cAccess_txtPwd"]')
        self.passwordForm.send_keys(password)

        self.submitButton = self.driver.find_element_by_xpath('//*[@id="ctl00_cAccess_btnLogin"]')
        self.submitButton.click()
        print(f'{self.appName} Logado com sucesso')

    def searchList(self, jobType="Jovem aprendiz"):
        """
        Go to main page and get the selected job
        :param jobType: Type of job - String
        :return: None
        """
        print(print(f'{self.appName} Selecionando vaga...'))
        try:
            self.searchJob = self.driver.find_element_by_xpath(
                '/html/body/form/div[3]/div[6]/section[1]/div/div/ol/li[1]/input')
        except:
            try:
                self.searchJob = self.driver.find_element_by_xpath(
                    '/html/body/form/div[4]/div[6]/section[1]/div/div/ol/li[1]/input')

            except:
                raise

        self.searchJob.send_keys(str(jobType))
        self.searchJob.send_keys(Keys.ENTER)
        print(f'{self.appName} Feito!, buscando vagas para {jobType}')

    def searchOptions(self):
        """
        Select the options to customize job options
        :return: None
        """
        print(f'{self.appName} Ajustando opções...')
        try:
            # Select to São Paulo
            self.cityOptionSaoPaulo = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_phMasterPage_cFacetLocation3_rptFacet_ctl01_chkItem"]').click()
            # Select CLT
            self.cltOption = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_phMasterPage_cFacetContractWorkType_rptFacet_ctl01_chkItem"]').click()

        except:
            sleep(10)
            #if falls, try to click again
            self.cltOption = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_phMasterPage_cFacetContractWorkType_rptFacet_ctl01_chkItem"]').click()

        sleep(10)
        print(f"{self.appName} Feito!")

    def getJob(self):
        """
        Get links from container of jobs to array and clicks one-by-one
        :return: none
        """
        print(f'{self.appName} Selecionando vagas disponiveis...')
        try:
            while True:
                sleep(5)
                
                #jobs container
                self.jobsContainer = self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_resultsGrid"]')
                # get links
                self.links = self.jobsContainer.find_elements_by_tag_name('a')
                for link in self.links:
                    #append to array
                    self.jobsLink.append(link.get_attribute('href').replace(',', ''))

                #click to links
                for target in self.jobsLink:
                    self.subscribeJob(target)
                

                self.driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_cGrid_Paginator1_lnkNext"]').click()

        except Exception as error:
            print(error)
            pass
            

    def subscribeJob(self, link):
        #get driver
        driver = self.driver

        driver.get(link)
        sleep(5)
        try:
            # click in link of jobs
            driver.find_element_by_xpath('//*[@id="ctl00_phMasterPage_cHeader_lnkCandidatar"]').click()
            sleep(5)
            # subscribe or not?
            print(f'{self.appName} Vaga cadastrada!')

            #back to jobs container
            driver.back()
            sleep(5)
            driver.back()

        except Exception as error:
            print(f'{self.appName} Link não encontrado!')
            pass

    def quitSearch(self):
        print(f'{self.appName} Saindo... volte sempre :)')
        self.driver.quit()

