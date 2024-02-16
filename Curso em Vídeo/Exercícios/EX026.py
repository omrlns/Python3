# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('ESCREVA UMA FRASE: ')).upper().strip()
print('EXITE {} "A" NA FRASE DIGITADA.' .format(frase.count('A')))
print('O PRIMEIRO "A" ESTÁ NA POSIÇÃO {}.' .format(frase.find('A') +1 ))
print('O ÚLTIMO "A" ESTÁ NA POSIÇÃO {}.' .format(frase.rfind('A') +1 ))

