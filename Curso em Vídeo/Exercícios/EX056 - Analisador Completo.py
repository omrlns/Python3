# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# no final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
 
somaIdade = 0
maiorIdadeHomem  = 0
nomeMaisVelho = ''
mulheresMenores20 = 0

for i in range(4):
    nome = input(f'Informe o nome da {i+1}ª primeira pessoa: ')
    sexo = input(f'Informe o sexo da {i+1}ª primeira pessoa (F = Feminino | M = Masculino): ')
    idade = int(input(f'Informe a idade da {i+1}ª primeira pessoa: '))
    somaIdade += idade
    if (i == 1 and sexo in 'Mm'):
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if (sexo in 'Mm' and idade > maiorIdadeHomem):
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if (sexo in 'Ff' and idade < 20):
        mulheresMenores20 += 1

mediaIdade = somaIdade / 4

print('\nA MÉDIA DE IDADE do grupo é: {} anos'.format((mediaIdade)))
print('O HOMEM MAIS VELHO tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeMaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheresMenores20))