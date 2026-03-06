# 3. dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares. 

valorN = int(input("informe o valor de n: "))

i = 0 # contador de ímpares impressos
valorImpar = 1

while i < valorN:
    print(valorImpar)
    i += 1
    valorImpar += 2

