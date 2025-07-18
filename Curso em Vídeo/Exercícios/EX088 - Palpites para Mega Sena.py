# faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# o programa vai perguntar quantos jogos serão gerados,
#  e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []
jogos = []

print('=' * 33)
print('          MEGA SENA          ')
print('=' * 33)
qJogos = int(input('informe a quantidade de jogos que você quer gerar? '))
total = 1
while total <= qJogos:
    contador = 0
    while True:
        numero = randint(1, 60)
        if (numero not in lista):
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('\n' + '=' * 5, 'SORTEANDO OS JOGOS', '=' * 5)
for i, l in enumerate(jogos):
    print('JOGO #{}: {}'.format(i + 1, sorted(l)))
    sleep(1)
print()

