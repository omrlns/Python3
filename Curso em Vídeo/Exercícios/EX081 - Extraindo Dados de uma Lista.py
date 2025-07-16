# crie um programa que vai ler vários números e colocar em uma lista.                  
# depois disso, mostre: 
# A) quantos números foram digitados.
# B) a lista de valores, ordenada de forma decrescente.
# C) se o valor 5 foi digitado e está ou não na lista.

valores = []
continuar = 'S'
contador = 0

while continuar == 'S':
    numero = int(input('digite um número: '))
    valores.append(numero)
    contador += 1    
    continuar = str(input('você deseja continuar? [S/N] ')).strip().upper()[0]
print('\nvocê digitou {} número(s)!'.format(contador))
print('números em ordem decrescente: {}'.format(sorted(valores, reverse=True)))
if (5 in valores):
    print('o número 5 está presente na lista!')
else:
    print('o número 5 não está presente na lista!')