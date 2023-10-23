#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = (co ** 2 + ca ** 2) ** (1/2)
from math import hypot
hipotenusa = hypot(co, ca)
print('O comprimento da hiponetusa é {:.2f}'.format(hi))
print('O comprimento da hiponetusa é {:.2f}'.format(hipotenusa))
