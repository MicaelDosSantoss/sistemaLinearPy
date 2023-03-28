# Como descobrir se um sistema é SPD, SPI é SI

import numpy as np

A = np.array([[7,-1,1],[2,1,-1],[3,-1,2]]) # Matriz dos coeficientes
# array | vectores é matrizes
B = np.array([3,0,6]) # termos independentes
Ax = np.array([[3,-1,1],[0,1,-1],[6,-1,2]])

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