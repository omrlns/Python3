# crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# no final, mostre a lista ordenada na tela.

valores = []
for i in range(5):
    numero = int(input('digite um número: '))
    if (i == 0 or numero > valores[-1]):
        valores.append(numero)
        print('valor inserido no final da lista!')
    else:
        posicao = 0
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                print('valor inserido na posição {}.'.format(posicao))
                break
            posicao += 1
print('\nos valores digitados em ordem foram: {}'.format(valores))