# desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

segmentoA = float(input('Informe o tamanho do segmento A: '))
segmentoB = float(input('Informe o tamanho do segmento B: '))
segmentoC = float(input('Informe o tamanho do segmento c: '))

if (segmentoA < segmentoB + segmentoC and segmentoB < segmentoA + segmentoC and segmentoC < segmentoA + segmentoB):
    print('Os segmentos podem formar um triângulo!')
else: 
    print('Os segmentos não podem formar um triângulo!')