# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valorCompra = float(input('Qual o valor do produto? R$'))
print('\nQUAL SERÁ A CONDIÇÃO DE PAGAMENTO? \n[1] - À VISTA NO DINHEIRO/CHEQUE \n[2] - À VISTA NO CARTÃO \n[3] - EM ATÉ 2X NO CARTÃO \n[4] - 3X OU MAIS NO CARTÃO')
escolha = int(input('DIGITE A OPÇÃO DESEJADA (1, 2, 3 ou 4): '))

if (escolha > 4):
    print('ERRO! INFORME UMA OPÇÃO CORRETA!')
    exit()
else:
    if (escolha == 1):
        print('\nVocê escolheu pagar À VISTA com DINHEIRO/CHEQUE, por isso iremos lhe dar um desconto de 10%')
        print('Valor sem desconto: R${:.2f}'.format(valorCompra))
        desconto = valorCompra - (valorCompra * 0.10)
        print('Valor com desconto aplicado: R${:.2f}'.format(desconto))
    elif (escolha == 2):
        print('\nVocê escolheu pagar À VISTA com CARTÃO, por isso iremos lhe dar um desconto de 5%')
        print('Valor sem desconto: R${:.2f}'.format(valorCompra))
        desconto = valorCompra - (valorCompra * 0.05)
        print('Valor com desconto aplicado: R${:.2f}'.format(desconto))
    elif (escolha == 3):
        print('\nVocê escolheu pagar no CARTÃO em ATÉ 2X')
        print('Valor à pagar: R${:.2f}'.format(valorCompra))
    elif (escolha == 4):
        print('\nVocê escolheu pagar no CARTÃO em 3X OU MAIS, por isso sua compra terá um acréscimo de 20% de juros')
        acrescimo = valorCompra + (valorCompra * 0.20)
        print('Valor à pagar: R${:.2f}'.format(acrescimo))