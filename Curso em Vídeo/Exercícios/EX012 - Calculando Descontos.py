#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual o valor do produto? R$'))
desconto = preço - (preço * 0.05)
print('Oba liquidação! Com desconto este produto vai lhe custar R${:.2f}'.format(desconto))