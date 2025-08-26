# este é um desafio que eu achei um pouco mais complexo e precisei da ajuda do mentor que lecionou a aula.
# porém, é algo que eu quero usar como estudo e entender um pouco mais a formatação e criação de parâmetros / métodos


import os, textwrap

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(): 
    menu = '''\n
================ MENU ================
[1]\tDEPOSITAR
[2]\tSACAR
[3]\tEXTRATO
[4]\tNOVA CONTA
[5]\tLISTAR CONTAS
[6]\tNOVO USUÁRIO
[7]\tSAIR

ESCOLHA UMA OPÇÃO PARA CONTINUAR
=> '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if (valor > 0):
        saldo += valor
        extrato += 'DEPÓSITO: \tR${:.2f}\n'.format(valor)
        print('\n===== SUCESSO, OPERAÇÃO EXECUTADA! =====')
    else:
        print('\n===== ERRO, INFORME UM VALOR VÁLIDO! =====')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeroSaques, limiteSaques):
    excedeuSaldo = valor > saldo
    excedeuLimite = valor > limite
    excedeuSaques = numeroSaques >= limiteSaques

    if (excedeuSaldo):
        print('\n===== ERRO! VOCÊ NÃO TEM SALDO SUFICIENTE!! =====')

    elif (excedeuLimite):
        print('\n===== ERRO! O VALOR DO SAQUE EXCEDE O LIMITE! =====')

    elif (excedeuSaques):
        print('\n===== ERRO! QUANTIDADE DE SAQUE EXCEDIDA, VOLTE AMANHÃ! =====')

    elif (valor > 0):
        saldo -= valor
        extrato += 'SAQUE:\t\tR$ {:.2f}\n'.format(valor)
        numeroSaques += 1
        print('\n===== SUCESSO, OPERAÇÃO EXECUTADA! =====')

    else:
        print('\n===== ERRO, INFORME UM VALOR VÁLIDO! =====')

    return saldo, extrato

def exibirExtrato(saldo, /, *, extrato):
    print('\n========== EXTRATO ==========')
    print('\nNENHUMA MOVIMENTAÇÃO FOI REALIZADA!' if not extrato else extrato)
    print('\nSALDO: R${:.2f}'.format(saldo))
    print("==========================================")
    input('\nAPERTE ENTER PARA CONTINUAR...')

def criarUsuario(usuarios):
    cpf = input('CPF (SOMENTE NÚMERO): ')
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print('\n===== ERRO, JÁ EXISTE UM USUÁRIO COM ESSE CPF! =====')
        return

    nome = input('NOME COMPLETO: ')
    dataNascimento = input('DATA DE NASCIMENTO (DD/MM/AAAA): ')
    endereco = input('ENDEREÇO: ')

    usuarios.append({'nome': nome, 'dataNascimento': dataNascimento, 'cpf': cpf, 'endereco': endereco})

    print("===== CADASTRO EFETUADO COM SUCESSO! =====")

def filtrarUsuario(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None

def criarConta(agencia, numeroConta, usuarios):
    cpf = input('CPF: ')
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print('\n===== CONTA CRIADA COM SUCESSO! =====')
        return {'agencia': agencia, 'numeroConta': numeroConta, 'usuario': usuario}

    print('\n===== ERRO, USUÁRIO NÃO ENCONTRADO! =====')

def listarContas(contas):
    for conta in contas:
        linha = f'''\
            AGÊNCIA:\t{conta['agencia']}
            C/C:\t\t{conta['numeroConta']}
            TITULAR:\t{conta['usuario']['nome']}
        '''
        print('=' * 75)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numeroSaques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if (opcao == '1'):
            valor = float(input('INFORME O VALOR DO DEPÓSITO: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif (opcao == '2'):
            valor = float(input('INFORME O VALOR DO SAQUE: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeroSaques=numeroSaques,
                limiteSaques=LIMITE_SAQUES,
            )

        elif (opcao == '3'):
            exibirExtrato(saldo, extrato=extrato)

        elif (opcao == '6'):
            criarUsuario(usuarios)

        elif (opcao == '4'):
            numeroConta = len(contas) + 1
            conta = criarConta(AGENCIA, numeroConta, usuarios)

            if (conta):
                contas.append(conta)

        elif (opcao == '5'):
            listarContas(contas)

        elif (opcao == '7'):
            break

        else:
            print('\n===== OPÇÃO INVÁLIDA! POR FAVOR, SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA! =====')

main()

