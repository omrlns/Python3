sexo = str(input('informe o seu sexo: [M] - Masculino ou [F] - Feminino: ')).strip().upper()[0]
while (sexo not in 'MmFf'):
    sexo = str(input('dados inválidos! informe o seu sexo corretamente: '))
print('sexo registrado com sucesso!')