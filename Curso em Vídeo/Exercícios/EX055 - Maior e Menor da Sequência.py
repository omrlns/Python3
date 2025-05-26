# faça um programa que leia o peso de cinco pessoas. 
# no final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range(5):
    peso = float(input(f'Informe o peso da {i+1}ª pessoa em Kg: '))
    pesos.append(peso)
 
print('O menor peso é: {}kg'.format(min(pesos)))
print('O maior peso é: {}kg'.format(max(pesos)))