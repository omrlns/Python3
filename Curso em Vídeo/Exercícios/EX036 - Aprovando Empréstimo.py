# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# a prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
tempo = int(input('Em quantos anos você pretende quitar a casa? '))

parcela = valorCasa / (12 * tempo) 

if (parcela > salario * 0.30):
    print('Empréstimo negado por insuficiência de renda!')
else:
    print('Parabéns, o seu empréstimo foi aprovado!')
    