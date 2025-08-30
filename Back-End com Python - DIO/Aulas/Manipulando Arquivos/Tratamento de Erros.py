from pathlib import Path

# try:
#     file = open('meu-arquivo.py')
# except FileNotFoundError as exc:
#     print('o arquivo não existe!')
#     print(exc)

ROOT_PATH = Path(__file__).parent
try:
    file = open(ROOT_PATH / 'teste')
except PermissionError as exc:
    print('não foi possível abrir o arquivo: \n{}'.format(exc))

