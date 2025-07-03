# faça um programa que leia um número qualquer e mostre o seu fatorial.
# exemplo:
# # 5! = 5 x 4 x 3 x 2 x 1 = 120

# from math import factorial

numero = int(input('informe um número para saber o seu fatorial: '))
# fatorial = factorial(numero)
auxiliar = numero
fatorial = 1
print('calculando... {}!...'.format(numero))

while (auxiliar > 0):
    print('{}'.format(auxiliar), end='')
    print(' x ' if auxiliar > 1 else ' = ', end='')
    fatorial *= auxiliar
    auxiliar -= 1
print('{}'.format(fatorial), end='')
# print('o fatorial de {} é {}.'.format(numero, fatorial))

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 