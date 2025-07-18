# crie um programa que vai ler vários números e colocar em uma lista. 
# depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

nValores = int(input('informe a quantidade de valores que você deseja digitar: '))
for i in range(nValores):
    numero = int(input(f'digite o {i+1}º número: '))
    numeros.append(numero)
    if (numero % 2 == 0):
        pares.append(numero)
    else:
       impares.append(numero)
print('\nvocê digitou os seguintes números: {}'.format(numeros))
if impares:
    print('dos valores informados, são ímpares: {}'.format(impares))
else:
    print('nenhum valor ímpar foi informado!')
if pares:
    print('dos valores informados, são pares: {}'.format(pares))
else:
    print('nenhum valor par foi informado!')
    