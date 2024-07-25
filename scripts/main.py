from web_scraper import coletar_dados, iniciar_driver
import os

def main():
    url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
    driver = iniciar_driver()

    for pagina in range(1, 51):
        url = url_base.format(pagina)
        dados = coletar_dados(driver, url)
        if dados:
            nome_arquivo = os.path.join('data', f'dados_pagina_{pagina}.txt')
            with open(nome_arquivo, 'w') as f:
                for item in dados:
                    f.write("%s\n" % item)
            print(f"Dados da página {pagina} salvos localmente em {nome_arquivo}")
        else:
            print(f"Nenhum dado encontrado na página {pagina}.")
    
    driver.quit()

if __name__ == "__main__":
    main()