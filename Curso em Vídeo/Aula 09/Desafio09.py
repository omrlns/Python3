#Manipulando Texto
frase = 'SÃO PAULO FC É GIGANTEEE!'
print(frase)
print(len(frase))
print(frase.count('O'))
print(frase.count('O', 4, 10))
print(frase.find('FC'))
print('GIGANTEEE' in frase)
print('NANICO' in frase)
mudanca = frase.replace('GIGANTEEE', 'O MAIOR TIME DO BRASIL')
print(mudanca)
# print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 = 'Ó TRICOLOR,           CLUBE           BEM           AMADOOO...          '
print(frase2)
mudanca2 = frase2.strip() #sem atribuição de espaço inútil?
print(mudanca2) #?
divisao = frase.split()
print(divisao[4])
print('💥'.join(frase))
print('-'.join(frase))

