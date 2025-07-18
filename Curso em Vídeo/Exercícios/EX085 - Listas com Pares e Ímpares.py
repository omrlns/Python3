# crie um programa onde o usuário possa digitar sete valores numéricos,
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# no final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'digite o {i}º valor: '))
    if (valor % 2 == 0):
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print()
print('dos valores digitados, são pares: {}'.format(sorted(numeros[0])))
print('dos valores digitados, são ímpares: {}'.format(sorted(numeros[1])))