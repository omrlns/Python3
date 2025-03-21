# escreva um programa que leia a velocidade de um carro. 
# se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# a multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Informe a velocidade atual do carro: '))

if (velocidade > 80):
    print('Você ultrapassou o limite de 80km/h e foi multado!')
    print('A multa lhe custará R${}'.format((velocidade - 80) * 7))
else:
    print('Você está dentro do limite! Boa viagem!')
