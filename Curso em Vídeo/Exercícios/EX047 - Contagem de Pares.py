# crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

numPares = []

for i in range(1, 51):
    if (i % 2 == 0):
        numPares.append(i)
print('\nOs números pares entre 1 e 50 são: \n{}'.format(numPares))