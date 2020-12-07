#1* conejo + 1 *gallina = 50 total animales
#4*conecjo + 2*gallina = 140 total patas


import numpy as an
a = np.array([[1,1],[4,2]])
r = np.array([50,140])
solucion = np.linalg.solve(a,r)
print(solucion)