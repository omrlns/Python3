def meuGerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 5

for i in meuGerador(numeros=[1, 3, 5, 7, 9]):
    print(i)

# se o código for mais simples, use gerador, se não, use iterador.