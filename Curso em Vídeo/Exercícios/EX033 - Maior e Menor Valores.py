# faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
