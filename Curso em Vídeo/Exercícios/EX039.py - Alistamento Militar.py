# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year
sexo = str(input('Sabendo que "F é feminino" e "M é Masculino", informe o seu sexo: '))
anoNasc = int(input('Informe o ano em que você nasceu: '))

idade =  anoAtual - anoNasc
print('Você nasceu em {} e tem {} anos.'.format(anoNasc, idade))

if (sexo.upper() == 'M'):
    if (idade == 18):
        print('É IMPORTANTE que você se aliste nesse ano!')
    elif (idade < 18):
        diferenca = 18 - idade
        print('Aguarde, ainda faltam {} anos para o alistamento!'.format(diferenca))
        alistamento = anoAtual + diferenca
        print('Seu alistamento será em {}, atente-se!'.format(alistamento))
    elif (idade > 18):
        diferenca = idade - 18
        print('Você deveria ter se alistado há {} anos!'.format(diferenca))
        alistamento = anoAtual - diferenca
        print('Seu alistamento foi em {}!'.format(alistamento))
else:
    print('Você é mulher, não precisa se alistar!')
