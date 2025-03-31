# escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Informe um número inteiro: '))
print('Qual será a base de conversão? Escolha:')
print('[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL')
tipoDeConversao = int(input('Informe uma opção: '))

if (tipoDeConversao == 1):
    print('{} convertido para BINÁRIO é {}'.format(numero, bin(numero) [2:]))
elif (tipoDeConversao == 2):
    print('{} convertido para OCTAL é {}'.format(numero, oct(numero) [2:]))
elif (tipoDeConversao == 3):
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero) [2:]))
else:
    print('Informe uma opção válida!')

