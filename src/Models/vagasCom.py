from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

    def insertJob(self, job="desenvolvedor front-end"):
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
        sleep(5)

        filterSp = driver.find_elements_by_partial_link_text('São Paulo')[0].click()
        sleep(5)
        filterJunior = driver.find_elements_by_partial_link_text('Júnior/Trainee')[0].click()
        sleep(5)
        print(f'{self.appName} Feito!')

    def quitSearch(self):
        print(f'{self.appName} Saindo... volte sempre :)')
        self.driver.quit()