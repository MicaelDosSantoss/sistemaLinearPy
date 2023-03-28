import numpy as np

a = np.array([[1,2,-1],[3,-4,5],[1,2,9]])
b = np.array([0,10,1])
Ax = np.array([[0,2,-1],[10,-4,5],[1,2,9]])



detA = np.linalg.det(a)
detAx = np.linalg.det(Ax)


if detA !=0:
  result = np.linalg.solve(a,b)
  print(f"SISTEMA POSSIVEL DETERMINADO - {result}")
else:
  if detA ==0 and detAx ==0:
    print("Sistema Possivel e Indeterminado")
  else:
    print("Sistema Impossivel")