# melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# o programa encerrará quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input('Informe o 1º TERMO da PA: '))
razao = int(input('Informe a RAZÃO da PA: '))

termo = primeiroTermo
contador = 1

total = 0
maisTermos = 10

while (maisTermos != 0):
    total += maisTermos
    while (contador <= total):
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA.')
    maisTermos = int(input('Você deseja ver mais quantos termos dessa progressão? '))
print('Progressão finalizada com {} termos.'.format(total))
