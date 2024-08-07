from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
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
        # Mapeia a classe de estrelas para um número
        estrelas_dict = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        estrelas_numero = estrelas_dict.get(estrelas, 0)
        
        # Adiciona o título, o preço e as estrelas à lista de dados
        dados.append({
            "title": titulo,
            "price": preco,
            "stars": estrelas_numero
        })
    
    return dados

def iniciar_driver():
    # Instala automaticamente o ChromeDriver compatível
    chromedriver_autoinstaller.install()
    return webdriver.Chrome()
