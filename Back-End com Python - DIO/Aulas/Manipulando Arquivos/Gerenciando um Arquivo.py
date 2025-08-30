import os, shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# os.mkdir(ROOT_PATH / 'Biblioteca') # cria uma nova pasta no caminho correto do meu projeto


# file = open(ROOT_PATH / 'arquivo-maneiro.txt', 'w')
# file.close()

# os.rename(ROOT_PATH / 'arquivo-maneiro.txt', ROOT_PATH / 'alterado.txt') # renomear o arquivo
# os.remove(ROOT_PATH / 'alterado.txt')
shutil.move(ROOT_PATH / 'exemplo.txt', 'Aulas\Manipulando Arquivos\Biblioteca')