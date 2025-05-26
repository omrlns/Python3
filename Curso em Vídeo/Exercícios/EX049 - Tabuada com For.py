# refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Você deseja saber a tabuada de qual número? '))
for i in range(1, 11):
    resultado = i * tabuada
    print(' {} x {} = {}'.format(i, tabuada, resultado))