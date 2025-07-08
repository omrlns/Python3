# faça um programa que jogue par ou ímpar com o computador. 
# o jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitoria = 0

while True:
    jogador = int(input('Informe um número para jogar: '))
    cpu  = randint(0, 10)
    total = jogador + cpu
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('Você jogou {} e a CPU jogou {}. O total foi {}.'.format(jogador, cpu, total), end='')
    print(' DEU PAR!' if total % 2 == 0 else ' DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            vitoria += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            vitoria += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print('GAME OVER! Você venceu {} vez(es)!'.format(vitoria))
    
