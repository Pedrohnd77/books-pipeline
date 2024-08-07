from web_scraper import coletar_dados, iniciar_driver
import os
import csv

def main():
    url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
    driver = iniciar_driver()

    # Validando se a pasta 'data' existe
    os.makedirs('data', exist_ok=True)

    for pagina in range(1, 51):
        url = url_base.format(pagina)
        dados = coletar_dados(driver, url)
        if dados:
            nome_arquivo = os.path.join('data', f'dados_pagina_{pagina}.csv')
            with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['title', 'price', 'stars']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for item in dados:
                    writer.writerow(item)
            print(f"Dados da página {pagina} salvos localmente em {nome_arquivo}")  
        else:
            print(f"Nenhum dado encontrado na página {pagina}.")
    
    driver.quit()

if __name__ == "__main__":
    main()