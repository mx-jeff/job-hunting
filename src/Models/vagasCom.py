from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from src.utils import timer, alert

from src.config import setSelenium
from src.credentails import vagasUser, vagasPassword
from src.utils.output import output


class VagasCom:
    appName = "[Job-hunting]"

    def __init__(self):
        self.driver = setSelenium("https://www.vagas.com.br")
        output(f'{self.appName} Iniciando...')

    def login(self):
        driver = self.driver
        
        try:
            output(f'{self.appName} Tentando logar...')

            # Click on login page
            driver.find_element_by_xpath('//*[@id="loginCandidatoDesktop"]').click()
            timer()

            # insert credentials and login-in
            driver.find_element_by_xpath('//*[@id="login_candidatos_form_usuario"]').send_keys(vagasUser)
            driver.find_element_by_xpath('//*[@id="login_candidatos_form_senha"]').send_keys(vagasPassword)
            driver.find_element_by_xpath('//*[@id="submitLogin"]').click()

        except Exception as error:
            output(f"{self.appName} Error: {error}")
            self.quitSearch()

        output(f'{self.appName} Logado com sucesso')
        timer()

    def insertJob(self, job):
        driver = self.driver

        output(f'{self.appName} A selecionar vaga...')
        # Insert a select job type and click it!
        inputJob = driver.find_element_by_xpath('//*[@id="nova-home-search"]')
        inputJob.send_keys(job)
        inputJob.send_keys(Keys.ENTER)
        timer()
        output(f'{self.appName} Vaga selecionada!')

    def searchOptions(self):
        # filter jobs-options
        output(f'{self.appName} A ajustar opções...')
        driver = self.driver
        timer()

        filterSp = driver.find_elements_by_partial_link_text('São Paulo')[0]
        driver.execute_script("arguments[0].click();", filterSp)
        
        timer()
        try:
            filterJunior = driver.find_elements_by_partial_link_text('Júnior/Trainee')[0]
            driver.execute_script("arguments[0].click();", filterJunior)

        except IndexError:
            output("Não há vagas para junior :(")
            pass

        output(f'{self.appName} Feito!')

    def selectJobs(self):
        output(f'{self.appName} Listando Vagas...')
        driver = self.driver

        container = driver.find_element_by_id('pesquisaResultado')
        #return container.get_attribute('outerHTML')

        links = container.find_elements_by_tag_name('a')

        # save all links 
        self.targetLink = [link.get_attribute('href') for link in links]
        
        output(f'{self.appName} Feito!')
        return self.targetLink

    @staticmethod
    def saveFile(html):
        with open('file.html','w') as file:
            file.write(html)

    def subscribeJob(self):
        output(f'{self.appName} Se inscrevendo na vaga...')
        driver = self.driver

        # Job page            
        for link in self.targetLink:
            driver.get(link)
            
            try:
                driver.find_element_by_name('bt-candidatura').click()
                
                try:
                    timer()
                    alert(driver)
                    driver.find_element_by_xpath('//*[@id="LtC"]/td[1]/table/tbody/tr/td[1]/a').click()
                    output(f'{self.appName} Inscrição realizada com sucesso :) ')
                    driver.back()
                    driver.back()

                except:
                    output(f'{self.appName} Inscrição realizada com sucesso :) ')
                    driver.back()
                
            except NoSuchElementException:
                output(f'{self.appName} Inscrição realizada anteriormente ;) ')
                driver.back()

            except Exception as error: 
                output(f'{self.appName} Erro na inscrição :( \nError: {error}')

            output(f'{self.appName} Feito!')

    def quitSearch(self):
        output(f'{self.appName} Saindo... volte sempre :)')
        self.driver.quit()