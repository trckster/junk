import numpy as np

matrix = [
    [6, 2, -3],
    [5, 1, 4],
    [2, 7, 1],
]

np_matrix = np.array(matrix)
answer = np.linalg.det(np_matrix)

print(round(abs(answer)))
