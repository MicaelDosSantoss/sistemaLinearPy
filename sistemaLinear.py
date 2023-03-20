import numpy as np


a = np.array([[2,-1],[1,5]]) # Matriz
b = np.array([7,-2]) # termos indepententes 
x = np.linalg.solve(a,b) #Resolução do sistema linear

print(x)