#Operadores Aritméticos

# + -> adição
# - -> subtração
# * -> multiplicação
# / -> divisão
# ** -> potência
# // -> divisão inteira
# % -> resto da divisão

#Ordem de Precedência

# 1º ()
# 2º **
# 3º *, /, //, %
# 4º +, -

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
multiplicação = n1 * n2
divisão = n1 / n2

divisãoInteira = n1 // n2
exponeciação = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(soma, multiplicação, divisão))
#podemos definir a quantidade de casas depois da vírgula da seguinte forma "{:.2f}"
print('A divisão inteira é {} e a potência é {}'.format(divisãoInteira, exponeciação))

#print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(soma, multiplicação, divisão), end=' ')
#pode se usar o "end=' '" para não se ter a quebra de linha entre um print e outro, mas também pode se ter um "\n" no meio do print para fazer a quebra de linha entre as informações.
#print('A divisão inteira é {} e a potência é {}'.format(divisãoInteira, exponeciação))
