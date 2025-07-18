# crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('digite uma expressão matemática com parênteses: '))
pilha = []
for caracter in expressao:
    if (caracter == '('):
        pilha.append('(')
    elif (caracter == ')'):
        if (len(pilha) > 0):
            pilha.pop()
        else:
            pilha.append(')')
            break
if (len(pilha) == 0):
    print('sua expressão matemática é válida!')
else:
    print('sua expressão matemática é inválida!')
