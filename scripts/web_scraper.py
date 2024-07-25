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
        # Seleciona o título do livro dentro do elemento 'article'
        titulo = elemento.find_element(By.TAG_NAME, 'h3').text

        # Seleciona o preço do livro dentro do elemento 'article'
        preco = elemento.find_element(By.CLASS_NAME, 'price_color').text 
        
        # Seleciona a quantidade de estrelas do livro
        estrelas_elemento = elemento.find_element(By.CSS_SELECTOR, 'p.star-rating')
        estrelas_classe = estrelas_elemento.get_attribute('class')
        
        # As classes de estrelas são 'star-rating One', 'star-rating Two', etc.
        estrelas = estrelas_classe.split()[-1]
        dados.append(f"{titulo} - {preco} - {estrelas}")
    
    return dados

def iniciar_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
