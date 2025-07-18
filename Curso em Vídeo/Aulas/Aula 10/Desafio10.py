# estrutura de condição simples
nome = input('Qual é seu nome? ')

if (nome == 'Marlon'):
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}!'.format(nome))

# média de um aluno
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

print('A sua média é {:.1f}'.format(media))

if (media >= 6):
    print('A sua média é boa, PARABÉNS!')
else:
    print('A sua média é ruim, ESTUDE MAIS!')