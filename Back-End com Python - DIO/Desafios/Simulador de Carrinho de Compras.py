# crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

# lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# entrada do número de itens
n = int(input().strip())

# loop para adicionar itens ao carrinho
for i in range(n):
    linha = input().strip()
    
    # encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: exiba os itens e o total da compra
# exibe cada item do carrinho com a formatação correta
for item, preco in carrinho:
    # formata o preço com duas casas decimais
    print(f"{item}: R${preco:.2f}")

# exibe o total da compra, também formatado
print(f"Total: R${total:.2f}")