import math
num = int(input('digite um número para saber a sua raiz: '))
raiz = math.sqrt(num)
#1 print padrão, sem formação de digítos e arredondamento
print('A raiz de {} é igual {}'.format(num, raiz))
#2 print com formatação de dígito (número de casas após a vírgula)
print('A raiz de {} é igual {:.2f}'.format(num, raiz))
#3 print com arrendondamento para cima
print('A raiz de {} é igual {}'.format(num, math.ceil(raiz)))
#4 print com arrendondamento para baixo
print('A raiz de {} é igual {}'.format(num, math.floor(raiz)))