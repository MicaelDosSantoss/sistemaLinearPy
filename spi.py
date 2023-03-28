# Sistema Possivel é indeterminado

import numpy as np

A = np.array([[1,1],[2,2]]) # Matriz dos coeficientes
# array | vectores é matrizes
B = np.array([4,8]) # termos independentes
Ax = np.array([[4,1],[8,2]])

# calculo determinantes

detA = np.linalg.det(A) # Determinante A
detAx = np.linalg.det(Ax) # Determinante detAx

#  analise dos determinantes

if detA != 0:
    result = np.linalg.solve(A,B)
    print(f'Sistema possível é determinado {result}')
else:
    if detA == 0 and detAx == 0:
        print('Sistema possível e indeterminado')
    else:
        print('Sistema Impossível')