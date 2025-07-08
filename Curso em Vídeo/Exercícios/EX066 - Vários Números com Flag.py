# crie um programa que leia números inteiros pelo teclado. 
# o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# no final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

numero = somatorio = contador = 0

while True:
    numero = int(input('Informe um número: '))
    if (numero == 999):
        break
    somatorio += numero
    contador += 1
print('Você digitou {} número(s)! O somatório dos números informados é: {}.'.format(contador, somatorio))