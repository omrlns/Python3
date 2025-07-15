# crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# inspirado no abecedário da xuxa
listagem = ('amor', 'baixinho', 'capacete', 'docinho', 'escola',
            'farofa', 'gente', 'humano', 'igualdade', 'juventude',
            'liberdade', 'molecagem', 'natureza', 'obrigado', 'professor', 
            'riacho', 'saudade', 'terra', 'universo', 'vida', 
            'xuxa', 'zumzumzum')

for palavra in listagem:
    print('\nna palavra: {}, temos '.format(palavra.upper()), end='')
    for letra in palavra:
        if (letra.lower() in 'aeiou'):
            print(letra, end=' ')