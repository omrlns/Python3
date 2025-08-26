# dicionário para agrupar participantes por tema
eventos = {}

# entrada do número de participantes
n = int(input().strip())

# loop para ler a entrada e preencher o dicionário
for _ in range(n):
    linha = input().strip()
    
    # encontra a última vírgula para separar o nome do tema, ou o espaço se não houver
    # esta linha é a mais robusta, pois lida tanto com "Nome, Tema" quanto "Nome Tema"
    posicao_separador = linha.rfind(",")
    if posicao_separador == -1:
        posicao_separador = linha.rfind(" ")

    participante = linha[:posicao_separador].strip()
    tema = linha[posicao_separador + 1:].strip()
    
    # se o tema ainda não está no dicionário, adiciona uma lista vazia
    if tema not in eventos:
        eventos[tema] = []

    # adiciona o participante à lista do tema correspondente
    eventos[tema].append(participante)

# --- exibe os grupos organizados ---
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")