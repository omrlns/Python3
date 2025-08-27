def meuDecorador(funcao):
    def conjunto(*args, **kargs):
        print('BEM-VINDO')
        funcao(*args, **kargs)
        print('ATÉ LOGO!')

    return conjunto

@meuDecorador  
def mensagem():
    print('OLÁ MUNDO!')

# mensagem = meuDecorador(mensagem) -> versão antes do @meuDecorador
mensagem()