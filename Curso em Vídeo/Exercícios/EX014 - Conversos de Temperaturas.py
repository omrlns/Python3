#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#Fórmula: (0 °C × 9/5) + 32 = 32 °F
c = float(input('Informe a temperatura em °C: '))
f = (c * 9 / 5) + 32
print('A temperatura de {} °C correponde a {}°F'.format(c, f))