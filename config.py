from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ


def setSelenium(link):
    options = Options()
    options.binary_location = environ.get('GOOGLE_CHROME_BIN')
    options.add_argument('--disable-notifications')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option("detach", True)
    path = environ.get("CHROMEDRIVER_PATH") or "./chromedriver.exe"

    driver = webdriver.Chrome(path, options=options)
    driver.get('http://www.infojobs.com.br')
    driver.implicitly_wait(10)

    return driver