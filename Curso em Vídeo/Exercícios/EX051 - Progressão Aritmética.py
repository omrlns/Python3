# desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# no final, mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input('Informe o 1º TERMO da PA: '))
razao = int(input('Informe a RAZÃO da PA: '))
print('\nOs 10 primeiros TERMOS da PA são:')
for i in range(10):
    termo = primeiroTermo + (i * razao)
    print('{}º termo: {}'.format(i+1, termo))