# faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# no final, mostre:

# A) quantas pessoas foram cadastradas.
# B) uma listagem com as pessoas mais pesadas.
# C) uma listagem com as pessoas mais leves.  

auxiliar = []
dados = []
maior = menor = 0

while True:
    auxiliar.append(str(input('informe o seu nome: ')).strip().lower())
    auxiliar.append(float(input('informe o seu peso em Kg: ')))
    if (len(dados) == 0):
        maior = menor = auxiliar[1]
    else:
        if (auxiliar[1] > maior):
            maior = auxiliar[1]
        if (auxiliar[1] < menor):
            menor = auxiliar[1]
    dados.append(auxiliar[:])
    auxiliar.clear()
    continuar = str(input('você deseja continuar? [S/N] ')).strip().lower()[0]
    if (continuar == 'n'):
        break
print('\nao todo, você cadastrou {} pessoa(s).'.format(len(dados)))
print('o maior peso foi de {}Kg. peso de '.format(maior), end='')
for pessoa in dados:
    if (pessoa[1] == maior):
        print('[{}] '.format(pessoa[0]), end='')
print()
print('o mennor peso foi de {}Kg. peso de '.format(menor), end='')
for pessoa in dados:
    if (pessoa[1] == menor):
        print('[{}] '.format(pessoa[0]), end='')
print()