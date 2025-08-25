# o método isdisjoint() é usado para verificar se dois conjuntos são disjuntos. 
# dois conjuntos são disjuntos se eles não têm nenhum elemento em comum. 
# a interseção entre eles é um conjunto vazio.  
# isso retorna True se os dois conjuntos não tiverem elementos em comum, 
# e False caso contrário.

A = {1, 2, 3, 4, 5}
B = {6, 7, 8, 9, 10}
C = {1, 2, 3}

print(A.isdisjoint(B)) # True
print(A.isdisjoint(C)) # False