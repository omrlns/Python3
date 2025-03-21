# escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# o programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
numeros = randint(0, 5)

palpite = int(input('Escolha um número entre 0 e 5: '))

if (palpite == numeros):
    print('Parabéns, você acertou!') 
else:
    print('Você errou! O número era {}'.format(numeros))

