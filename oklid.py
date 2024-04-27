import numpy as np

point1 = np.array((1, 2, 3))
point2 = np.array((1, 1, 1))

sum_sq = np.sum(np.square(point1 - point2))
 
print(np.sqrt(sum_sq))