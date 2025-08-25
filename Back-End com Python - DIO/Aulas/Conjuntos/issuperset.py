# o método issuperset() verifica se um conjunto é um superconjunto de outro. 
# um conjunto A é um superconjunto de um conjunto B 
# se todos os elementos de B também estão em A. 
# isso retorna True se A for um superconjunto de B, e False caso contrário.

A = {1, 2, 3}
B = {1, 2}
C = {1, 4}

# A é um superconjunto de B? sim, pois todos os elementos de B estão em A.
print(A.issuperset(B))  # saída: True

# B é um superconjunto de A? não, pois A tem o elemento 3.
print(B.issuperset(A))  # Saída: False

# A é um superconjunto de C? não, pois C tem o elemento 4.
print(A.issuperset(C))  # saída: False