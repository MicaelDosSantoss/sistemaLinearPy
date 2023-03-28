import numpy as np

# 5 exercicio

a = np.array([[2,-1,1],[1,-1,2],[1,1,1]])
b = np.array([3,3,6])
Ax = np.array([[3,-1,1],[3,-1,2],[6,1,1]])
Ay = np.array([[2,3,1],[1,3,2], [1,6,1]])

detA = np.linalg.det(a)
detX = np.linalg.det(Ax)


if detA != 0:
    result = np.linalg.solve(a,b)
    print(f'Sistema possível determinado - {result}')
else:
    if detA == 0 and detX == 0 :
        print('Sistema possível e Indeterminado')
    else:
        print('sistema impossivel')
