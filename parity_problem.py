import numpy as np

input_matrix = [[1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
self_weights = [-0.05, -0.02, 0.1, 0.03]
activations = np.dot(input_matrix, self_weights)

print(activations)

print(np.where(activations>0, 1, 0))


