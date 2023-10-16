#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivoe todas as suas informações possíveis sobre ele.

a = input('Digite algo:')
print('O tipo primitivo desse valor é', type(a))
print('Este valor só tem espaços?', a.isspace())
print('Este valor é um número?', a.isnumeric())
print('Este valor é alfabético?', a.isalpha())
print('Este valor é alfanumérico?', a.isalnum())
print('Este valor está em MAIÚSCULAS?', a.isupper())
print('Este valor está em minúsculas?', a.islower())
print('Este valor está capitalizado?', a.istitle())

