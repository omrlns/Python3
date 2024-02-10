#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('Verificando o número {}, podemos dizer que o seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))

