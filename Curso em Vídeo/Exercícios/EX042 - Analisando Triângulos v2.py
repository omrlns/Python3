# refaça o DESAFIO 35 dos triângulos, 
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

ladoA = float(input('Informe o tamanho do primeiro lado: '))
ladoB = float(input('Informe o tamanho do segundo lado: '))
ladoC = float(input('Informe o tamanho do terceiro lado: '))

# processamento & saída
if (ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA):
    print('\nOs valores formam um triângulo!')
    if (ladoA == ladoB == ladoC):
        print('O triângulo é equilátero, ou seja, possui três lados iguais!')
    
    elif (ladoA == ladoB or ladoA == ladoC or ladoB == ladoC):
        print('O triângulo é isósceles, ou seja, possui dois lados iguais!')

    else:
        print('O triângulo é escaleno, ou seja, possui três lados diferentes!')

else:
    print('Os valores não formam um triângulo!')