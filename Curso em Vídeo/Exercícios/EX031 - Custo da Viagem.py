# desenvolva um programa que pergunte a distância de uma viagem em Km. 
# calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem? '))

if (distancia <= 200):
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print('A passagem para essa viagem custará R${:.2f}'.format(passagem))