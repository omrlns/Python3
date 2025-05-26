# crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

somaMaiores = 0
somaMenores = 0
idadeDosMaiores = []
idadeDosMenores = []

for i in range(7):
    anoNasc = int(input(f'Informe o ANO DE NASCIMENTO da {i+1}ª pessoa: '))
    idade = date.today().year - anoNasc
    if (idade >= 21):
        idadeDosMaiores.append(idade)
        somaMaiores += 1
    else:
        idadeDosMenores.append(idade)
        somaMenores += 1
print('\n{} pessoas MAIORES de idade'.format(somaMaiores))
print('Idade dos Maiores: {}'.format(idadeDosMaiores))
print('\n{} pessoas MENORES de idade'.format(somaMenores))
print('Idade dos Menores: {}'.format(idadeDosMenores))
