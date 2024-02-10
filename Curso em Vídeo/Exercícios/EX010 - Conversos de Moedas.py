#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
saldo = float(input('Quanto dinheiro você tem na carteira? R$'))
dólar = saldo / 5.05
print('Com R${:.2f} você pode comprar US${:.2f}'.format(saldo, dólar))
