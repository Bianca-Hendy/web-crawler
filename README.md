# WEB - CRAWLER

# PYTHON
    O código utiliza o framework Scrapy para extrair informações de cursos do site da Alura. Ele inicia a raspagem na URL especificada, encontra os elementos HTML que representam os cursos usando seletor CSS, extrai o nome, link, imprime essas informações e salva em um arquivo CSV chamado "cursos.csv". O código é organizado em uma classe AluraBot que herda da classe scrapy.Spider e define a lógica de raspagem na função parse.

    Para utilizar é necessário instalar o scrapy com o comando 
    pip install scrapy