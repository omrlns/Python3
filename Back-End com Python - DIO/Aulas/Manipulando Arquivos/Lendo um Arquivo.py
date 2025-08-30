#  ler todo o conteúdo do arquivo de uma vez
file = open('exemplo.txt', 'r') # não vai rodar por conta da posição do arquivo
print(file.read())
print(file.readline()) # lê o arquivo linha por linha
print(file.readlines()) # lê tudo, porque retorna o item como uma lista completa
file.close
