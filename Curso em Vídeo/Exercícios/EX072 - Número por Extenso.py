# crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'catorze', 'quinze', 
               'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('\ninforme um número entre 0 e 20: '))
    if (numero >= 0 and numero <= 20):
        break
    print('\ntente novamente com um número válido!')
print('\nvocê digitou {}, e por extenso fica: "{}".'.format(numero, contExtenso[numero]))
        