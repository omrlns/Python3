# faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

tot = 0
numero = int(input('Informe um número: '))
for i in range(1, numero+1):
    if (numero % i == 0):
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
print('\n\033[mO número {} foi divisível {} vezes!'.format(numero, tot))
if (tot == 2):
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!') 