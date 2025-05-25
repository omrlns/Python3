# a Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Informe o ano de nascimento do(a) atleta: '))

idade = anoAtual - anoNasc

if (idade <= 9):
    print('A idade do(a) atleta é {} anos e sua categoria é MIRIM!'.format(idade))
elif (idade > 9 and idade <= 14):
    print('A idade do(a) atleta é {} anos e sua categoria é INFANTIL!'.format(idade))
elif (idade > 14 and idade <= 19):
    print('A idade do(a) atleta é {} anos e sua categoria é JÚNIOR!'.format(idade))
elif (idade > 19 and idade <= 25):
    print('A idade do(a) atleta é {} anos e sua categoria é SÊNIOR!'.format(idade))
elif (idade > 25):
    print('A idade do(a) atleta é {} anos e sua categoria é MASTER!'.format(idade))