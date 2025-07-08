# faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# o programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Você deseja ver a tabuada de qual número? '))
    if (numero < 1):
        print('Programa encerrado!')
        break
    for i in range(1, 11):
        print('{} x {} = {}'.format(numero, i, numero * i))