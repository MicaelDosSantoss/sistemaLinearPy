import numpy as np

# 1 exercicio

a = np.array([[2,-1],[1,5]]) # Matriz
b = np.array([7,-2]) # termos indepententes 
Ax = np.array([[7,-1], [-2,5]])

detA = np.linalg.det(a)
detAx = np.linalg.det(Ax)


# codigo para ver se o sistema é possível ou não

if detA != 0:
    result = np.linalg.solve(a,b)
    print(f"SISTEMA POSSIVEL DETERMINADO - {result}")
# f para incoporar valor a uma variavel {}
else:
    if detA ==0 and detAx ==0:
        print("Sistema Possivel e Indeterminado")
    else:
        print("Sistema Impossivel") 
