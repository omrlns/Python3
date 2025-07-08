# crie um programa que leia o nome e o preço de vários produtos. 
# o programa deverá perguntar se o usuário vai continuar ou não. 
# no final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totalCompra = produtos1000 = 0
produtoCaro = ''
maiorValor = 0

while True:
    produto = str(input('\nINFORME O NOME DO PRODUTO: '))
    valor = float(input('INFORME O VALOR DO PRODUTO: R$'))
    if valor >= 1000:
        produtos1000 += 1
    if valor > maiorValor:
        maiorValor = valor
        produtoCaro = produto

    totalCompra += valor

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nVOCÊ DESEJA CONTINUAR? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('\n# TOTAL DA COMPRA: R${:.2f}'.format(totalCompra))
print('# {} PRODUTO(S) CUSTAM MAIS DE R$1000'.format(produtos1000))
print('# O PRODUTO MAIS CARO É: "{}" E CUSTA R${:.2f}'.format(produtoCaro, maiorValor))
