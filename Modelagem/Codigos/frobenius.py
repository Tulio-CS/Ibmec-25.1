import numpy as np


m = np.array([[1,1/2,1/3], [1/2, 1/3,1/4], [1/3, 1/4,1/5]])

print(np.linalg.norm(m)*np.linalg.norm(np.linalg.inv(m)))