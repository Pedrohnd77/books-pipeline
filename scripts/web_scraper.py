from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def coletar_dados(driver, url):
    driver.get(url)
    time.sleep(5)  # Tempo de espera para a página carregar
    
    
    elementos = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
    dados = []
    
    for elemento in elementos:
        titulo = elemento.find_element(By.TAG_NAME, 'h3').text
        preco = elemento.find_element(By.CLASS_NAME, 'price_color').text
        dados.append(f"{titulo} - {preco}")
    
    return dados

def iniciar_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
