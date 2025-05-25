# crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

print('{:=^40}'.format(' DESAFIO JOKENPÔ ')) # :^20 é uma formatação especial
print('''ESCOLHA ENTRE:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogadorEscolha = int(input('Qual é a sua jogada? '))
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
cpuEscolha = randint(0, 2)

print('')
print('/-/' * 10)
print('O computador escolheu {}'.format(opcoes[cpuEscolha]))
print('O jogador escolheu {}'.format(opcoes[jogadorEscolha]))
print('/-/' * 10)

if (cpuEscolha == 0): #cpu escolheu pedra
    if (jogadorEscolha == 0): #jogador escolheu pedra
        print('\nEMPATE!')
    elif (jogadorEscolha == 1): #jogador escolheu papel
        print('\nJOGADOR VENCEU!')
    elif (jogadorEscolha == 2): #jogador escolheu tesoura
        print('\nCOMPUTADOR VENCEU!')
    else:
        print('\nJOGADA INVÁLIDA. TENTE NOVAMENTE!')
elif (cpuEscolha == 1): #cpu escolheu papel
    if (jogadorEscolha == 0): #jogador escolheu pedra
        print('\nCOMPUTADOR VENCEU!')
    elif (jogadorEscolha == 1): #jogador escolheu papel
        print('\nEMPATE!')
    elif (jogadorEscolha == 2): #jogador escolheu tesoura
        print('\nJOGADOR VENCEU!')
    else:
        print('\nJOGADA INVÁLIDA. TENTE NOVAMENTE!')
if (cpuEscolha == 2): #cpu escolheu tesoura
    if (jogadorEscolha == 0): #jogador escolheu pedra
        print('\nJOGADOR VENCEU!')
    elif (jogadorEscolha == 1): #jogador escolheu papel
        print('\nCOMPUTADOR VENCEU!')
    elif (jogadorEscolha == 2): #jogador escolheu tesoura
        print('EMPATE!')
    else:
        print('\nJOGADA INVÁLIDA. TENTE NOVAMENTE!')

