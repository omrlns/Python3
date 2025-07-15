#  crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, 
# na ordem de colocação. 
# depois mostre:
# a) os 5 primeiros times.
# b) os últimos 4 colocados.
# c) times em ordem alfabética.
# d) em que posição está o time da chapecoense

times = ('São Paulo', 'Grêmio', 'Cruzeiro', 'Palmeiras', 
         'Flamengo', 'Internacional', 'Botafogo', 'Goiás', 
         'Coritiba', 'Vitória', 'Sport Recife', 'Atlético-MG', 
         'Athletico-PR', 'Fluminense', 'Santos', 'Náutico', 
         'Figueirense', 'Vasco da Gama', 'Portuguesa', 'Ipatinga')

print('TIMES QUE PARTICIPARAM DA "SÉRIE A" EM 2008: \n{}'.format(times))
# a) os 5 primeiros times.
print('\nO TOP5 DESSA EDIÇÃO FOI: \n{}'.format(times[0:5]))
# b) os últimos 4 colocados.
print('\nOS REBAIXADOS PARA "SÉRIE B" FORAM: \n{}'.format(times[-4:]))
# c) times em ordem alfabética.
print('\nTIMES EM ORDEM ALFABÉTICA: \n{}'.format(sorted(times)))
# d) em que posição está o time da São Paulo
print('\nO SÃO PAULO TERMINOU O CAMPEONATO NA {}ª POSIÇÃO!'.format(times.index('São Paulo') + 1))


