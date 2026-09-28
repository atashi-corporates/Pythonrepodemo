import numpy as np

M = np.array([
    [2, 0],
    [0, 2]
])

P = np.array([2, 3])

result = M @ P

print("New Position:", result)