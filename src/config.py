from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ
import os
import sys

from src.utils.selenium_path import resource_path
from factory import ROOT_DIR


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def setSelenium(link):
    options = Options()
    options.binary_location = environ.get('GOOGLE_CHROME_BIN')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-logging")
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')

    path = environ.get('CHROMEDRIVER_PATH') or resource_path(os.path.join(ROOT_DIR, "chromedriver.exe"))

    driver = webdriver.Chrome(path, options=options)
    driver.get(link)
    driver.implicitly_wait(10)

    return driver



configVar = {
    'graphInferface': False,
    'cli': False,
    'command': True
}
