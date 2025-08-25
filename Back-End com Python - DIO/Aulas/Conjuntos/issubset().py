# o método issubset() verifica se um conjunto é um subconjunto de outro. 
# um conjunto A é um subconjunto de um conjunto B 
# se todos os elementos de A também estão em B. 
# isso retorna True se A for um subconjunto de B, e False caso contrário.

A = {1, 2, 8}
B = {1, 2, 3, 8, 9, 0}

print(A.issubset(B)) # True
print(B.issubset(A)) # False