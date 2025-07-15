# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('os valores sorteados foram: ', end='')
for i in numeros:
    print('{} '.format(i), end='')
print('\no maior valor sorteado foi: {}'.format(max(numeros)))
print('o menor valor sorteado foi: {}'.format(min(numeros)))
