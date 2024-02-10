#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Por quantos dias o carro foi alugado? '))
distância = float(input('Quantos quilômetros foram percorridos? '))
diária = dias * 60
km = distância * 0.15
total = diária + km
print('O carro foi alugado por {} dias.'.format(dias))
print('O carro percorreu uma distância de {:.1f} km.'.format(distância))
print('O valor total do serviço a se pagar é R${:.2f}'.format(total))
