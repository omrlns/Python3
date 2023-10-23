#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O angulo de {}° tem o SENO de {:.2f}'.format(ângulo, seno))
print('O angulo de {}° tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
print('O angulo de {}° tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
