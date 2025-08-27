def meuDecorador(funcao):
    def conjunto():
        print('BEM-VINDO')
        funcao()
        print('ATÉ LOGO!')

    return conjunto

@meuDecorador  
def mensagem():
    print('OLÁ MUNDO!')

# mensagem = meuDecorador(mensagem) -> versão antes do @meuDecorador
mensagem()