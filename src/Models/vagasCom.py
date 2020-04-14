from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

from src.config import setSelenium
from src.credentails import vagasUser, vagasPassword


class VagasCom:
    appName = "[Job-hunting]"

    def __init__(self):
        self.driver = setSelenium("https://www.vagas.com.br")
        print(f'{self.appName} Iniciando...')

    def login(self):
        driver = self.driver
        
        try:
            print(f'{self.appName} Tentando logar...')

            # Click on login page
            driver.find_element_by_xpath('//*[@id="loginCandidatoDesktop"]').click()
            sleep(5)

            # insert credentials and login-in
            driver.find_element_by_xpath('//*[@id="login_candidatos_form_usuario"]').send_keys(vagasUser)
            driver.find_element_by_xpath('//*[@id="login_candidatos_form_senha"]').send_keys(vagasPassword)
            driver.find_element_by_xpath('//*[@id="submitLogin"]').click()

            print(f'{self.appName} Logado com sucesso')
            sleep(5)

        except Exception as error:
            print(f"{appName} Error: {error}")
            self.quitSearch()

    def insertJob(self, job):
        driver = self.driver

        print(f'{self.appName} A selecionar vaga...')
        # Insert a select job type and click it!
        inputJob = driver.find_element_by_xpath('//*[@id="nova-home-search"]')
        inputJob.send_keys(job)
        inputJob.send_keys(Keys.ENTER)
        sleep(5)
        print(f'{self.appName} Vaga selecionada!')

    def searchOptions(self):
        # filter jobs-options
        print(f'{self.appName} A ajustar opções...')
        driver = self.driver

        filterSp = driver.find_elements_by_partial_link_text('São Paulo')[0].click()
        sleep(5)
        filterJunior = driver.find_elements_by_partial_link_text('Júnior/Trainee')[0].click()
                    
        print(f'{self.appName} Feito!')

    def selectJobs(self):
        print(f'{self.appName} Listando Vagas...')
        driver = self.driver

        container = driver.find_element_by_id('pesquisaResultado')
        #return container.get_attribute('outerHTML')

        links = container.find_elements_by_tag_name('a')

        # save all links 
        self.targetLink = [link.get_attribute('href') for link in links]
        
        print(f'{self.appName} Feito!')
        return self.targetLink

    @staticmethod
    def saveFile(html):
        with open('file.html','w') as file:
            file.write(html)

    def subscribeJob(self):
        print(f'{self.appName} Se inscrevendo na vaga...')
        driver = self.driver

        # Job page            
        for link in self.targetLink:
            driver.get(link)
            
            try:
                driver.find_element_by_name('bt-candidatura').click()
                print(f'{self.appName} Inscrição realizada com sucesso :) ')
                driver.back()

            except:
                try:
                    driver.find_element_by_xpath('//*[@id="LtC"]/td[1]/table/tbody/tr/td[1]/a').click()
                    print(f'{self.appName} Inscrição realizada com sucesso :) ')
                    driver.back()
                    driver.back()
                
                except NoSuchElementException:
                    print(f'{self.appName} Inscrição realizada anteriormente ;) ')
                    driver.back()

                except: 
                    print(f'{self.appName} Erro na inscrição :(')


            print(f'{self.appName} Feito!')

    def quitSearch(self):
        print(f'{self.appName} Saindo... volte sempre :)')
        self.driver.quit()