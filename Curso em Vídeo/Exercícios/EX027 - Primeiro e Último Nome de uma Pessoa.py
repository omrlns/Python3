# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('digite o seu nome completo: ')).strip()
n = nome.split()
print('olá!')
print('seu primeiro nome é {}' .format(n[0]))
print('seu segundo nome é {}' .format(n[len(n) - 1]))      
