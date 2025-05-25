# crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

notas = []

for i in range(2):
    nota = float(input(f'Informe a {i + 1}ª nota do aluno(a): '))
    notas.append(nota)

media = ( notas[(0)] + notas[(1)] ) / 2

if (media < 5):
    print('\nAluno(a) REPROVADO(A)!')
elif (media == 5 and media <= 6.9):
    print('\nAluno(a) em RECUPERAÇÃO!')
else:
    print('\nAluno(a) APROVADO(A)!')