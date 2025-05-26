# faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

somaMultiplos = 0

for i in range(1, 500):
    if (i % 2 != 0):
        if (i % 3 == 0):
            somaMultiplos += i
print('\nA somatória dos números impares múltiplos de 3 é: {}'.format(somaMultiplos))
