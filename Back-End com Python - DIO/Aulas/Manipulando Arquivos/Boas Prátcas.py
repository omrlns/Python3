from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'teste.txt', 'r') as file:
 1 / 0
print(file.read())
