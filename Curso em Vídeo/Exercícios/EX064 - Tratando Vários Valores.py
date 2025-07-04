# crie um programa que leia vários números inteiros pelo teclado. 
# o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
contador = 0

while True:
    numero = int(input('Informe um número aleatório ou digite 999 para parar: '))
    if (numero != 999):
        soma += numero
        contador += 1
    else:
        print('Você digitou {} número(s) e a soma deles é igual a {}.'.format(contador, soma))