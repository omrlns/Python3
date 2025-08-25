numeros = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10}

# conjuntos em python não suportam indexação e nem fatiamento, 
# caso queira acessar os seus valores é necessário converter o conjunto para lista.
numeros = list(numeros)

print(numeros[0]) # 1