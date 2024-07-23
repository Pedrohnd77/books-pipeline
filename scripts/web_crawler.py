from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def coletar_dados(driver, url):
    driver.get(url)
    time.sleep(5)
    elementos = driver.find_elements(By.CLASS_NAME, 'classe-dos-elementos')
    dados = [elem.text for elem in elementos]
    return dados

def iniciar_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
