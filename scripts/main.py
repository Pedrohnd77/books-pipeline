from web_scraper import coletar_dados, iniciar_driver
from s3_uploader import upload_para_s3
import os

def main():
    url_base = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    pagina_atual = 1
    driver = iniciar_driver()

    #while True:
    url = url_base #+ str(pagina_atual)
    dados = coletar_dados(driver, url)
    if dados:
        #break
        nome_arquivo = f'dados_pagina_{pagina_atual}.txt'
        with open(nome_arquivo, 'w') as f:
            for item in dados:
                f.write("%s\n" % item)
        print(f"Dados salvos localmente em {nome_arquivo}")
    else:
        print("Nenhum dado encontrado na página.")
    #upload_para_s3(nome_arquivo, 'bookswebscraper')
    #os.remove(nome_arquivo)
    #pagina_atual += 1

    driver.quit()

if __name__ == "__main__":
    main()
