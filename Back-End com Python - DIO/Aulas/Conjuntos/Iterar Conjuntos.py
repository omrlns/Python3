# a forma mais comum para percorrer os dados de um conjunto é utilizando o comando for.
carros = {'gol', 'celta', 'palio'}

for indice, carro in enumerate(carros):
    print('{}: {}'.format(indice, carro))
    
# saída
# 0: gol
# 1: celta
# 2: palio