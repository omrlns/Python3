# crie um programa que leia a idade e o sexo de várias pessoas. 
# a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# no final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiorIdade = totalHomens = totalMulheres20 = 0

while True:
    idade = int(input('\nIDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiorIdade += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMulheres20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('VOCÊ DESEJA CONTINUAR? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print('\nQUANTIDADE DE PESSOAS MAIORES DE IDADE: {}'.format(maiorIdade))
print('QUANTIDADE DE HOMENS CADASTRADOS: {}'.format(totalHomens))
print('QUANTIDADE MULHERES COM MENOS DE 20 ANOS: {}'.format(totalMulheres20))