# crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

valorA = int(input('digite o primeiro valor: '))
valorB = int(input('digite o segundo valor: '))

opcao = 0
while (opcao != 5):
    print('''\n[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
''')
    opcao = int(input('QUAL É A OPÇÃO? '))
    if (opcao == 1):
        soma = valorA + valorB
        print('\n{} + {} = {}'.format(valorA, valorB, soma))
    elif (opcao == 2):
        produto = valorA * valorB
        print('\n{} * {} = {}'.format(valorA, valorB, produto))
    elif (opcao == 3):
        if (valorA > valorB):
            maior = valorA
        else:
            maior = valorB
        print('\nO VALOR MAIOR É: {}'.format(maior))
    elif (opcao == 4):
        valorA = int(input('digite o primeiro valor: '))
        valorB = int(input('digite o segundo valor: '))
    else:
        print('\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
    sleep(2)
print('\nVOCÊ SAIU DO PROGRAMA!')