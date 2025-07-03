# refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiroTermo = int(input('Informe o 1º TERMO da PA: '))
razao = int(input('Informe a RAZÃO da PA: '))

termo = primeiroTermo
contador = 1

while (contador <= 10):
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM.')