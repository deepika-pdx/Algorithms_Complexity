import math


def findMedian(A, B):
    n = len(A)
    if n == 1:
        median = (A[0] + B[0]) / 2
        return median
    elif n == 2:
        median = (max(A[0], B[0]) + min(A[1], B[1])) / 2
        return median
    while n > 2:
        if (n % 2) != 0:
            m1 = A[math.floor((n - 1) / 2)]
            m2 = B[math.floor((n - 1) / 2)]
        elif (n % 2) == 0:
            m1 = A[math.floor(n / 2)]
            m2 = B[math.floor(n / 2)]
        # Checking if median values are equal
        if m1 == m2:
            median = (m1 + m2) / 2
            return median
        elif m1 < m2:
            m1_index = A.index(m1)
            m2_index = B.index(m2)
            return findMedian(A[m1_index:n], B[0:m2_index + 1])
        else:
            m1_index = A.index(m1)
            m2_index = B.index(m2)
            return findMedian(A[0:m1_index + 1], B[m2_index:n])
    return -1


A = [1, 2, 3, 6]
B = [4, 6, 8, 10]
# A = [1, 12, 15, 26, 38]
# B = [2, 13, 17, 30, 45]
print(findMedian(A, B))
