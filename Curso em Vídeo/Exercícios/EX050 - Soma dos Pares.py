# desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# se o valor digitado for ímpar, desconsidere-o.

somatorio = 0
for i in range(0, 6):
    numero = int(input(f'Informe o {i+1}º número: '))
    if (numero % 2 == 0):
        somatorio += numero
print('\nConsiderando apenas os números pares, o somatório é: {}'.format(somatorio))