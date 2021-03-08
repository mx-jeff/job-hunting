from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ

from src.utils.selenium_path import resource_path


def setSelenium(link):
    options = Options()
    options.binary_location = environ.get('GOOGLE_CHROME_BIN')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-logging")
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')

    path = "./chromedriver.exe" or environ.get('CHROMEDRIVER_PATH')

    driver = webdriver.Chrome(path, options=options)
    driver.get(link)
    driver.implicitly_wait(10)

    return driver


configVar = {
    'graphInferface': False,
    'cli': False,
    'command': True
}
