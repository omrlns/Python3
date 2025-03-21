# faça um programa que leia um ano qualquer e mostre se ele é bissexto.

def anoBissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

ano = int(input('Digite um ano: '))
if anoBissexto(ano):
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))
