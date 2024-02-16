# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('DIGITE O NOME DA SUA CIDADE: '))
# validacao ='SANTO' in cidade.upper()
# print('BUSCAMOS POR "SANTO" NO NOME DA SUA CIDADE E O RESULTADO É {}' .format(validacao))
print(cidade[0:5] == 'SANTO')




