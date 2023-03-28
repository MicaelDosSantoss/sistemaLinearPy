import numpy as np

a = np.array([[1,2],[2,-3]])
b = np.array([5,-4])
aX = np.array([[5,2],[-4,-3]])


detA = np.linalg.det(a)
detX = np.linalg.det(aX)

if detA != 0:
    result = np.linalg.solve(a,b)
    print(f'Sistema possível e determinado {result}')
else:
    if detA == 0 and detX == 0:
        print('Sistema possível e indeterminado')
    else:
        print('Sistema impossível')