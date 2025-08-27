def meuDecorador(funcao):
    def conjunto():
        print('BEM-VINDO')
        funcao()
        print('ATÉ LOGO!')

    return conjunto
    
def mensagem():
    print('OLÁ MUNDO!')

mensagem = meuDecorador(mensagem)
mensagem()