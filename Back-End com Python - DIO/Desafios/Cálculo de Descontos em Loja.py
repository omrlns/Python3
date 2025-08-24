# dicionário com os valores de desconto
descontos = {
    'DESCONTO10': 0.10,
    'DESCONTO20': 0.20,
    'SEM_DESCONTO': 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: aplique o desconto se o cupom for válido:

if cupom in descontos:
    
    if (cupom == 'DESCONTO10'):
        preco -= (preco * descontos['DESCONTO10'])
        print('{:.2f}'.format(preco))
    
    elif (cupom == 'DESCONTO20'):
        preco -= (preco * descontos['DESCONTO20'])
        print('{:.2f}'.format(preco))
        
    elif (cupom == 'SEM_DESCONTO'):
        preco -= (preco * descontos['SEM_DESCONTO'])
        print('{:.2f}'.format(preco))
    