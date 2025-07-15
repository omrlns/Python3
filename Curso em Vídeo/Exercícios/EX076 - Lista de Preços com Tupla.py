# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Notebook Dell G15 5510', 6000,
            'Monitor LG', 750,
            'Mouse Red Dragon', 250,
            'Mousepad Red Dragon', 100,
            'Headset JBL', 300)

print('-' * 40)
print('{:^40}'.format('TABELA DE PREÇOS'))
print('-' * 40)
for i in range(0, len(produtos)):
    if (i % 2 == 0):
        print('{:.<30}'.format(produtos[i]), end='')
    else:
        print('R${:>7.2f}'.format(produtos[i]))