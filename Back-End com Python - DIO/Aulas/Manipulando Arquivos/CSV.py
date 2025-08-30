import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# try:
#     with open(ROOT_PATH / 'registros.csv', 'w', encoding='utf-8') as file:
#         escritor = csv.writer(file)
#         escritor.writerow(['id', 'nome'])
#         escritor.writerow(['1', 'Marlon'])
#         escritor.writerow(['2', 'Taíse'])
# except IOError as fail:
#     print('erro ao criar o arquivo. \n{}'.format(fail))

try:
    with open(ROOT_PATH / 'registros.csv', 'r', newline='',  encoding='utf-8') as file:
        leitor= csv.reader(file)
        for row in leitor:
            print(row)
except IOError as fail:
    print('erro ao ler o arquivo. \n{}'.format(fail))