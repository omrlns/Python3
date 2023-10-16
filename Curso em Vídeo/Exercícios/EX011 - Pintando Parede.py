#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².
largura = float(input('Informe em metros a largura da parede que você deseja pintar: '))
altura = float(input('Informe em metros a altura da parede que você deseja pintar: '))
area = largura * altura
tinta = area / 2
print('A sua parede tem {:.2f} m² e você vai precisar de {:.1f} l de tinta para pintá-la.'.format(area, tinta))