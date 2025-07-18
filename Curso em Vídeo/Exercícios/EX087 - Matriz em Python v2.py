# aprimore o desafio anterior, mostrando no final:

# A) a soma de todos os valores pares digitados.
# B) a soma dos valores da terceira coluna.
# C) o maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = maior = somaColuna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um valor para [{linha}, {coluna}]: '))
print('=' * 33)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print('[{:^5}]'.format(matriz[linha][coluna]), end='')
        if (matriz[linha][coluna] % 2 == 0):
            somaPares += matriz[linha][coluna]
    print()
print('=' * 33)
print('a soma dos valores pares é: {}'.format(somaPares))
for linha in range(0, 3):
    somaColuna += matriz[linha][2]
print('a soma dos valores da terceira coluna é: {}'.format(somaColuna))
for coluna in range(0, 3):
    if (coluna == 0):
        maior = matriz[1][coluna]
    elif (matriz[1][coluna] > maior):
        maior = matriz[1][coluna]
print('o maior valor da segunda linha é: {}'.format(maior))
print('=' * 33)

