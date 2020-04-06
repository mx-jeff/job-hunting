from selenium import webdriver
from src.config import setSelenium
from src.credentails import vagasUser, vagasPassword
from time import sleep


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

    def quitSearch(self):
        print(f'{self.appName} Saindo... volte sempre :)')
        self.driver.quit()