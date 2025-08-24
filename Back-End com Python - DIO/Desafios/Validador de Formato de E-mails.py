def validar(email):

    '''
    regras: 
    1 - deve conter o caractere "@" e um domínio    
    2 - não pode começar ou terminar com "@"  
    3 - não pode conter espaços
    '''

    if ('@' not in email) or (email.startswith("@") or email.endswith("@")) or (" " in email):
        return 'E-mail inválido'

    # verifica se há um domínio após o @
    if (len(email.split("@")) != 2) or ("." not in email.split("@")[1]):
        return 'E-mail inválido'

    # se passou por todas as verificações, o e-mail é válido
    return 'E-mail válido'
    
while True:
  try:
    email_input = input() # lê a entrada fornecida automaticamente (funciona na plataforma da dio)
    resultado = validar(email_input)  # chama a função de validação
    print(resultado)  # exibe o resultado da validação 
  except EOFError: break 