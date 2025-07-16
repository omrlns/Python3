# faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# no final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
for n in range(5):
    numero = int(input(f'digite o {n+1}º número: '))
    valores.append(numero)

print('\ndos números digitados, o maior é {}, e o menor é {}'.format(max(valores), min(valores)))
print('\no maior valor está localizado na posição: ', end='')
for i, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{i}... ', end='')
print('\no menor valor está localizado na posição: ', end='')
for i, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{i}... ', end='')