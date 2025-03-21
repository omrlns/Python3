# crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Informe um número inteiro para saber se ele é Ímpar ou Par: '))

if (numero % 2 == 0):
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))