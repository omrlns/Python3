# melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
numero = randint(1, 10)
print('========== JOGO DE ADIVINHAÇÃO ==========')
palpiteJogador = int(input('TENTE ADIVINHAR! diga um número de 1 a 10: '))
contador = 0

while (palpiteJogador != numero):
    palpiteJogador = int(input('ERROOOU! tente novamente: '))
    contador += 1

print('\nPARABÉNS, o número era {} e você o acertou em {} tentativas!'.format(numero, contador))

