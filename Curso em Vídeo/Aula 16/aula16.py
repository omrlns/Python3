lanches = ('hotdog', 'calzone', 'coxinha', 'donuts', 'pudim')
bebidas = ('suco', 'água', 'café', 'refrigerante', 'chá')
# tuplas são imutáveis, logo, não podem receber novos valores depois de definidas
# lanches[1] = 'bacon' ou bebidas[3] = 'vodka', são mudanças que o programa não vai aceitar por conta da regra anterior

for comida in lanches:
    print('hoje eu vou almoçar "{}"'.format(comida))
print('\ncaramba, tô satisfeito!!!'.upper())

