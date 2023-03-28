import numpy as np

# exercicio 7

# contas com porcentagem pode ser feitas apenas em percentual
A = np.array([[0.15, 0.1 , 0.06],[1,1,-1],[1,1,1]])
B = np.array([20000,0,200000])
x = np.array([[20000, 0.1 , 0.06],[0,1,-1],[200000,1,1]])

detA = np.linalg.det(A)
detAx = np.linalg.det(x)

if detA != 0:
    result = np.linalg.solve(A,B)
    print(f'Sistema possível é determinado {result}')
else:
    if detA == 0 and detAx == 0:
        print('Sistema possível e indeterminado')
    else:
        print('Sistema Impossível')