import numpy as np

T = np.array([
    [1, 0, 0, 2],
    [0, 1, 0, 3],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])

P = np.array([1, 2, 0, 1])

new_P = T @ P

print("Original Point:", P)
print("Transformed Point:", new_P)