#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
aluno1 = str(input('Digite o nome de um aluno: '))
aluno2 = str(input('Digite o nome de outro aluno: '))
aluno3 = str(input('Digite o nome de outro aluno: '))
aluno4 = str(input('Digite o nome de outro aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print('Parabéns {}! Você foi escolhido(a) para apagar o quadro.'.format(sorteio))

