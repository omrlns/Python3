# for i in range(1, 6):
#     print('Oi Marlon!')
# print('Acabou!')

# print('')

# for i in range(1, 6):
#     print('\n{}'.format(i))
# print('\nFim!')

# for i in range(5, 0, -1):
#     print('\n{}'.format(i))
# print('\nFim!')

# numero = int(input('Informe um número: '))
# for i in range(0, numero+1):
#     print(i)
# print('Acabou, rs!')

# inicio = int(input('Início: '))
# fim = int(input('Fim: '))
# pulo = int(input('Pulo: '))
# for i in range(inicio, fim+1, pulo):
#     print(i)
# print('Acabou, rs!')

somatorio = 0
for i in range(0, 5):
    numero = int(input(f'Informe o {i+1}º número: '))
    somatorio += numero
print('O somatório de todos os valores é: {}'.format(somatorio))