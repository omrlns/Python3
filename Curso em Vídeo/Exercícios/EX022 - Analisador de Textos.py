#Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

#Lógica pensada para o nome: Marlon da Silva
# nome = input('Qual é o seu nome? ')
# print('Olá {}!' .format(nome))
# print('Assim fica o seu nome se todas as letras forem maiúsculas: {}' .format(nome.upper()))
# print('Assim fica o seu nome se todas as letras forem minúsculas: {}' .format(nome.lower()))
# divisao = nome.split()
# a = len(divisao[0])
# b = len(divisao[1])
# c = len(divisao[2])
# soma = a + b + c
# print('O seu nome completo tem {} letras.' .format(soma))
# print('O seu primeiro nome tem {} letras.' .format(a))

#Correção
nome = str(input('Qual é o seu nome? ')).strip()
print('Olá {}!' .format(nome))
print('Assim fica o seu nome se todas as letras forem maiúsculas: {}' .format(nome.upper()))
print('Assim fica o seu nome se todas as letras forem minúsculas: {}' .format(nome.lower()))
print('O seu nome completo tem {} letras.' .format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.' .format(nome.find(' ')))

