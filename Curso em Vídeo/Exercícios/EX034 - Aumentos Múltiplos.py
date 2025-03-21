#escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# para salários superiores a R$1250,00, calcule um aumento de 10%. 
# para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o seu salário: R$'))

if (salario > 1250):
    salarioNovo = salario + salario * 0.10
    print('Você recebeu um aumento de 10% e o seu novo salário será R${:.2f}'.format(salarioNovo))
elif (salario <= 1250):
    salarioNovo = salario + salario * 0.15
    print('Você recebeu um aumento de 15% e o seu novo salário será R${:.2f}'.format(salarioNovo))
else:
    print('HAHAHA você é estagiário!')