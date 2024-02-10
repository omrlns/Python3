#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Qual é o salário do funcionário? R$'))
reajuste = salário * 15 / 100
aumento = salário + reajuste
print('O salário do funcionário é R${:.2f}, mas após o aumento de 15% passará a ser R${:.2f}'.format(salário, aumento))