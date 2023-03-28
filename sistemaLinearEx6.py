import numpy as np

# 6 exercicio

a = np.array([[1,4,7], [2,3,6], [5,1,-1]])
b = np.array([2,2,8])
Ax = np.array([[2,4,7],[2,3,6],[8,1,-1]])

detA = np.linalg.det(a)
detX = np.linalg.det(Ax)

if detA != 0:
    result = np.linalg.solve(a,b)
    print(f'Sistema possível determinado- {result}')
else:
    if detA == 0 and detX == 0:
        print('Sistema possível e indeterminado')
    else:
        print('sistema impossivel')