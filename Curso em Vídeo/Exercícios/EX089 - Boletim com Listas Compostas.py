# crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# no final, mostre um boletim contendo a média de cada um,
#  e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = []
while True:
    nome = str(input('NOME: ')).strip().upper()
    nota1 = float(input(f'INFORME A 1ª NOTA DO(A) "{nome}": '))
    nota2 = float(input(f'INFORME A 2ª NOTA DO(A) "{nome}": '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    continuar = str(input('QUER CONTINUAR? [S/N] '))
    if (continuar in 'Nn'):
        break
print('=' * 33)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('=' * 33)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('=' * 33)
    opcao = int(input('MOSTRAR NOTAS DE QUAL ALUNO? (333 INTERROMPE): '))
    if (opcao == 333):
        print("ENCERRANDO PROGRAMA...")
        break
    if (opcao <= len(ficha) - 1):
        print(f'NOTAS DE {ficha[opcao][0]} SÃO {ficha[opcao][1]}')