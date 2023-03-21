import numpy as np

a = np.array([[1,2,-1],[3,-4,5],[1,2,9]])
b = np.array([0,10,1])
Ax = np.array([[0,2,-1],[10,-4,5],[1,2,9]])
Ay = np.array([[1,0,-1],[3,10,5],[1,1,9]])


detA = np.linalg.det(a)
detAx = np.linalg.det(Ax)
detAy = np.linalg.det(Ay)

if detA !=0:
  result = np.linalg.solve(a,b)
  print(f"SISTEMA POSSIVEL DETERMINADO - {result}")
else:
  if detA ==0 and detAx ==0 and detAy ==0:
    print("Sistema Possivel e Indeterminado")
  else:
    print("Sistema Impossivel")