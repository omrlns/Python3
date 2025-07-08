# crie um programa que simule o funcionamento de um caixa eletrônico. 
# no início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 

# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format('SIMULADOR DE CAIXA ELETRÔNICO'))
print('=' * 30)

valor = int(input('INFORME O VALOR QUE VOCê DESEJA SACAR: R$'))

total = valor
cedulaAtual = 50
totalCedula = 0

while True:
    if (total >= cedulaAtual):
        total -= cedulaAtual
        totalCedula += 1
    else:
        if (totalCedula > 0):
            print('TOTAL DE {} CÉDULA(S) DE R${}'.format(totalCedula, cedulaAtual))
        if (cedulaAtual == 50):
            cedulaAtual = 20
        elif (cedulaAtual == 20):
            cedulaAtual = 10
        elif (cedulaAtual == 10):
            cedulaAtual = 1
        totalCedula = 0
        if (total == 0):
            break