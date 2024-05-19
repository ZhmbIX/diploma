import numpy as np

x = np.array([[4,6,1,2],
     [5, np.inf, 0, 0]])

N_1u = np.copy(x[x.T[1]>6])

print(N_1u)