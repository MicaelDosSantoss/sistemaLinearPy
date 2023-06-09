import numpy as np

a = np.array([[1,1],[2,2]])
b = np.array([5,10])
aX = np.array([[5,1],[10,2]])

detA = np.linalg.det(a)
detX = np.linalg.det(aX)

if detA != 0:
    result = np.linalg.solve(a,b)
    print(f'Sistema possível determinado {result}')
else:
    if detA == 0 and detX == 0:
        print('Sistema possível e indeterminado')
    else:
        print('Sistema impossível')