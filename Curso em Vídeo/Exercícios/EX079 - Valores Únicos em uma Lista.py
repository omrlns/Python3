# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. # caso o número já exista lá dentro, ele não será adicionado. 
# no final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
continuar = 'S'
while continuar == 'S':
    valor = int(input('digite um número: '))
    if (valor in valores):
        print('proibido valor duplicado!')
    else:
        valores.append(valor)
    continuar = str(input('você deseja continuar? [S/N] ')).strip().upper()[0]
print('\nos valores digitados em ordem crescente são: {}'.format(sorted(valores)))
