# 2.  dado um número inteiro positivo n, calcular a soma dos n primeiros números inteiros positivos.

valorN = int(input("informe o valor de n: "))

soma, i = 0, 0

while i <= valorN:
    soma += i
    i += 1

print("\na soma do(s) {} primeiro(s) inteiro(s) positivo(s) é {}".format(valorN, soma))