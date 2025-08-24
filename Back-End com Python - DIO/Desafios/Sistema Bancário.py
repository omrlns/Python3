from time import sleep
import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

menu = '''

======= SISTEMA BANCÁRIO =======

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

ESCOLHA UMA OPÇÃO PARA CONTINUAR
=> '''

saldo, nSaque = 0, 0
limiteSaque = 500
extrato = ''
saqueDiario = 3

while True:

    opcao = input(menu)
    if (opcao == '1'):
        limparTerminal()
        print('\n====== SESSÃO DE DEPÓSITO ======')
        valor = float(input('\nINFORME O VALOR DO DEPÓSITO: R$'))
        limparTerminal()
        
        if (valor > 0):
            saldo += valor
            extrato += 'DEPÓSITO: R${:.2f}\n'.format(valor)

        else:
            print('ERRO! TENTE NOVAMENTE COM UM VALOR VÁLIDO!')
    
    elif (opcao == '2'):
        limparTerminal()
        print('\n====== SESSÃO DE SAQUE ======')
        valor = float(input('\nINFORME O VALOR DO SAQUE: R$'))

        valorMaior = valor > saldo # valorMaior será válido se o valor informado for maior que o saldo disponível
        limiteInvalido = valor > limiteSaque # limiteInvalido será válido se o valor informado for maior que o limite de saque de R$500
        qntdSaque = nSaque > saqueDiario # qntdSaque será valido se a quantidade de saques realizados for maior que 3, que é o máximo por dia / execução do programa

        if (valorMaior):
            limparTerminal()
            print('ERRO! VOCÊ NÃO TEM SALDO SUFICIENTE!')
            sleep(3)
            limparTerminal()

        elif (limiteInvalido):
            limparTerminal()
            print('ERRO! O VALOR DO SAQUE EXCEDE O LIMITE!')
            sleep(3)
            limparTerminal()

        elif (qntdSaque):
            limparTerminal()
            print('ERRO! QUANTIDADE DE SAQUE EXCEDIDA, VOLTE AMANHÃ!')
            sleep(3)
            limparTerminal()

        elif (valor > 0):
            limparTerminal()
            saldo -= valor
            extrato += 'SAQUE: R${:.2f}\n'.format(valor)
            nSaque += 1
            limparTerminal()
        
        else:
            print('ERRO! TENTE NOVAMENTE COM UM VALOR VÁLIDO!')

    elif (opcao == '3'):
        limparTerminal()
        print('\n====== SESSÃO DE EXTRATO ======')
        print('\nNENHUMA MOVIMENTAÇÃO FOI REALIZADA!' if not extrato else extrato)
        print('\nSALDO: R${:.2f}'.format(saldo))
        input('\nAPERTE ENTER PARA CONTINUAR...')
        limparTerminal()


    elif (opcao == '4'):
        limparTerminal()
        print('SAINDO DO PROGRAMA... VOLTE SEMPRE!')
        sleep(3)
        limparTerminal()
        break

    else:
        limparTerminal()
        print('\nOPÇÃO INVÁLIDA! POR FAVOR, SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA!')
        sleep(5)
        limparTerminal()
