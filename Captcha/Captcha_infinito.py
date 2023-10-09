import undetected_chromedriver as uc
from a_selenium_iframes_crawler import Iframes
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = uc.Chrome(options=options)
driver.get(r"https://sia.estacio.br/sianet/Logon")

