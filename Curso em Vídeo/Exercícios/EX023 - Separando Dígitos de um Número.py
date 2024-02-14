# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('INFORME UM NÚMERO: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('ANALISANDO O NÚMERO {}' .format(numero))
print('UNIDADE: {}' .format(unidade))
print('DEZENA: {}' .format(dezena))
print('CENTENA: {}' .format(centena))
print('MILHAR: {}' .format(milhar))


