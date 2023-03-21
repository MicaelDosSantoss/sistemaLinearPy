import numpy as np

a = np.array([[2,-1,1],[1,-1,2],[1,1,1]])
b = np.array([3,3,6])
Ax = np.array([[3,-1,1],[3,-1,2],[6,1,1]])
Ay = np.array([[2,3,1],[1,3,2], [1,6,1]])

detA = np.linalg.det(a)
detX = np.linalg.det(Ax)
detY = np.linalg.det(Ay)

if detA != 0:
    result = np.linalg.solve(a,b)
    print(f'Sistema possível - {result}')
else:
    if detA == 0 and detX == 0 and detY == 0:
        print('Sistema possível e determinado')
    else:
        print('sistema impossivel')
