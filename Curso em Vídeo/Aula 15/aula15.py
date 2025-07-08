numero = somatorio = 0

while True:
    numero = int(input('Informe um número: '))
    if (numero == 999):
        break
    somatorio += numero
print('O somatório dos números informados é: {}.'.format(somatorio))