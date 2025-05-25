# desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – acima de 40: Obesidade Mórbida

peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em metros: '))

imc = peso / (altura**2)

print('Seu IMC é: {:.2f}'.format(imc))

if (imc < 18.5):
    print('Você está ABAIXO DO PESO!')
elif (imc >= 18.5 and imc < 25):
    print('Você está no PESO IDEAL!')
elif (imc >= 25 and imc <= 30):
    print('Você se encontra em SOBREPESO!')
elif (imc > 30 and imc <= 40):
    print('Você está com grau de OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')
