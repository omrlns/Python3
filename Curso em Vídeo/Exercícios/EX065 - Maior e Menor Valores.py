# crie um programa que leia vários números inteiros pelo teclado. 
# no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numeros = []
contador = soma = media = 0
continuar = 'S'

while (continuar == 'S'):
    numero = int(input('Informe um número: '))
    contador += 1
    soma += numero
    numeros.append(numero)
    media = soma / contador
    continuar = str(input('Você deseja continuar? ')).upper().strip()[0]

if numeros:
    maior = max(numeros)
    menor = min(numeros)
    print('Você digitou {} número(s)! A média entre eles é {:.2f}.'.format(contador, media))
    print('Dos números informados, o maior é {} e o menor é {}.'.format(maior, menor))
else:
    print('Nenhum número foi informado.')
