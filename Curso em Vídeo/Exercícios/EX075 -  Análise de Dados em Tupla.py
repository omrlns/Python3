# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# no final, mostre:
# A) quantas vezes apareceu o valor 9.
# B) em que posição foi digitado o primeiro valor 3.
# C) quais foram os números pares.

numeros = (int(input('informe o 1º valor: ')),
           int(input('informe o 2º valor: ')),
            int(input('informe o 3º valor: ')),
             int(input('informe o 4º valor: ')),
              int(input('informe o 5º valor: ')))

print('\nvocê digitou os seguintes valores: {}'.format(numeros))
print('o "NÚMERO 9" apareceu {} vez(es).'.format(numeros.count(9)))
if (3 in numeros):
    print('o "NÚMERO 3" está na {}ª posição.'.format(numeros.index(3) + 1))
else:
    print('o "NÚMERO 3" não foi digitado!')
print('os números pares digitados foram: ', end='')
for i in numeros:
    if (i % 2 == 0):
        print(i, end=' ')
