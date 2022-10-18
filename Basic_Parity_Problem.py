import math

import numpy as np

input_matrix = [[1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0],
                [1, 1, 1, 1]]
self_weights = [-0.05, -0.02, 0.04, 0.05]
target = [1, 0, 0, 1, 0, 1, 1, 0]
eta = 0.1
epoch = 50
for e in range(epoch):
    print("----------------Epoch " + str(e) + "-----------------------------")
    count_t = 0
    for i in input_matrix:
        print(i)
        print(self_weights)
        wx = np.dot(i, np.transpose(self_weights))
        print("wx: " + str(wx))
        if wx > 0:
            y = 1
        else:
            y = 0
        t = target[count_t]
        print("t: " + str(t))
        print("y: " + str(y))
        if y == t:
            print("target matched")
            count_t = count_t + 1
            continue
        else:
            count_s = 0
            for s in self_weights:
                s = s - (eta * (y - t) * i[count_s])
                s = round(s, 2)
                self_weights[count_s] = s
                count_s = count_s + 1
        print("updated weight:", self_weights)
        count_t = count_t + 1
