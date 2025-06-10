numero = 1
nPar = 0
nImpar = 0

while (numero != 0):
    numero = int(input('digite um valor: '))
    if (numero != 0):
        if (numero % 2 == 0):
            nPar += 1
        else:
            nImpar += 1

print('você digitou {} valores ímpares e {} valores pares!'.format(nImpar, nPar))