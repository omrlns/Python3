# 1.  dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados.

numero = int(input("informe um número: "))

while numero != 0: # se o usuário informar 0, o programa se encerrará
    quadrado = numero * numero
    print("{}² = {}".format(numero, quadrado))
    numero = int(input("informe um número: "))

    