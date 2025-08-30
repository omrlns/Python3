import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'database.sqlite')
cursor = conexao.cursor()

def createTable(conexao, cursor):
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));'
        )
    conexao.commit()
    
def insert(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', data)
    conexao.commit()

def uptade(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()

# insert(conexao, cursor, 'Gustavo', 'gustavo@gamer.com')

# uptade(conexao, cursor, 'Marlon', 'marlon@dev.com', 1)
# uptade(conexao, cursor, 'Taíse', 'taise@dev.com', 2)

def delete(conexao, cursor, id):
    data = (id,) # é necessário colocar uma vírgula depois do valor quando for uma tupla com um único registro
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()

# delete(conexao, cursor, 3)

def manyInsert(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?);', dados)
    conexao.commit()

# dados = (['Tiago', 'tiago@dev.com'], ['Samuel', 'samuel@dev.com'], ['Cristyan', 'cristyan@dev.com'])
# manyInsert(conexao, cursor, dados)

def selectClient(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?;', (id,))
    return cursor.fetchone()

# cliente = selectClient(cursor, 1)
# print(cliente)

def allClients(cursor):
    cursor.row_factory = sqlite3.Row
    # return cursor.execute('SELECT * FROM clientes;')
    return cursor.execute('SELECT * FROM clientes ORDER BY nome;')

clientes = allClients(cursor)
for cliente in clientes:
    print(dict(cliente))
