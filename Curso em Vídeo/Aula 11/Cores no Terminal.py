# 1
print('\033[4;30;41mHello World!\033[m')

# 2
nome = 'Marlon' 
print('Olá {}{}{}! É um prazer te conhecer!'.format('\033[4;33m', nome, '\033[m'))

# 3
cores = {
    'limpa': '\033[m',  'amarelo': '\033[33m'
}

print('Uiuiui {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))