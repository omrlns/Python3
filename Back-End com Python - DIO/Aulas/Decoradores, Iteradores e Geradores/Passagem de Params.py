def mensagem(nome):
    print('EXECUTANDO MENSAGEM!')
    return 'OI {}!'.format(nome)


def mensagemLonga(nome):
    print('EXECUTANDO UMA MENSAGEM UM POUCO MAIOR!')
    return 'OLÁ {}, TUDO BEM COM VOCÊ?'.format(nome)


def executar(funcao, nome):
    print('EXECUTANDO A EXECUÇÃO DO EXECUTAR!')
    return funcao(nome)

print(executar(mensagem, 'MARLON'))
print(executar(mensagemLonga, 'MARLON'))