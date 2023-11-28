# Importa as bibliotecas necessárias do Scrapy e CSV
import scrapy
import csv

# Lista vazia para armazenar os cursos
cursos = []

# Define a classe da aranha (spider) AluraBot
class AluraBot(scrapy.Spider):
    # Nome da aranha
    name = "alura"

    # URLs iniciais a serem raspadas
    start_urls = ["https://www.alura.com.br/cursos-online-programacao"]

    # Função que é chamada para processar a resposta inicial da solicitação
    def parse(self, response):
        # Seletor CSS para encontrar os elementos que representam os cursos na página
        SELETOR = ".subcategoria__item"

        # Itera sobre cada categoria de curso encontrada na página
        for categoria in response.css(SELETOR):
            # Dicionário para armazenar informações do curso
            curso = {}

            # Seletor CSS para extrair o nome do curso
            NOME_SELETOR = ".card-curso__nome ::text"
            curso['nome'] = categoria.css(NOME_SELETOR).extract_first()

            # Seletor CSS para extrair o link do curso
            LINK_SELETOR = ".card-curso ::attr(href)"
            curso['link'] = "https://www.alura.com.br" + categoria.css(LINK_SELETOR).extract_first()

            # Seletor CSS para extrair a carga horária do curso
            CARGA_SELETOR = ".card-curso__carga ::text"
            curso['carga horaria'] = categoria.css(CARGA_SELETOR).get()

            # Imprime as informações do curso
            print(curso)

            # Adiciona o curso à lista de cursos
            cursos.append(curso)

        # Abre um arquivo CSV para escrita
        with open('cursos.csv', 'w') as csv_file:
            # Cria um objeto writer CSV
            writer = csv.writer(csv_file)

            # Itera sobre cada curso e escreve as informações no arquivo CSV
            for curso in cursos:
                writer.writerow(curso.values())

            # Imprime o total de cursos encontrados
            print("Total de Cursos: ", len(cursos))
