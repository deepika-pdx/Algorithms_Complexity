def BFMaxSubarraySum(A):
    n = len(A)
    maxSum = 0
    maxSubArray = []
    for i in range(n):
        currentSum = A[i]
        currentSubarray = [A[i]]
        for j in range(i + 1, n):
            currentSum = currentSum + A[j]
            currentSubarray.append(A[j])
            if currentSum > maxSum:
                maxSum = currentSum
                maxSubArray = currentSubarray.copy()
        if currentSum > maxSum:
            print(i)
            maxSum = currentSum
            maxSubArray = currentSubarray.copy()
    return maxSubArray


A = [-2, 1, -3, 4, -1, 2, 1, -6, 5]
print(BFMaxSubarraySum(A))

# def DCFindMaxCrossSubArray(A, low, mid, high):
#     left_sum = 0
#     sum = 0
#     max_left = 0
#     max_right = 0
#     for i in range(mid, low, -1):
#         sum = sum + A[i]
#         if sum > left_sum:
#             left_sum = sum
#             max_left = i
#
#     right_sum = 0
#     sum = 0
#     for j in range(mid + 1, high, 1):
#         sum = sum + A[j]
#         if sum > right_sum:
#             right_sum = sum
#             max_right = j
#     return (max_left, max_right, left_sum + right_sum)
#
#
# def DCFindMaxSubArray(A, low, high):
#     if high == low:
#         return (low, high, A[low])
#     else:
#         mid = math.floor((low + high) / 2)
#         (left_low, left_high, left_sum) = DCFindMaxSubArray(A, low, mid)
#         (right_low, right_high, right_sum) = DCFindMaxSubArray(A, mid + 1, high)
#         (cross_low, cross_high, cross_sum) = DCFindMaxCrossSubArray(A, low, mid, high)
#         if left_sum >= right_sum and left_sum >= cross_sum:
#             return (left_low, left_high, left_sum)
#         elif right_sum >= left_sum and right_sum >= cross_sum:
#             return (right_low, right_high, right_sum)
#         else:
#             return (cross_low, cross_high, cross_sum)
#
#
# A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# n = len(A)
# low = 0
# high = 0
# maxSum = 0
# (low, high, maxSum) = DCFindMaxSubArray(A, 0, n - 1)
# print(A[low: high + 1])

#
# def DPFindMaxSubArray(A):
#     n = len(A)
#     start = 0
#     end = 0
#     maxSum = A[0]
#     maxSoFar = A[0]
#
#     for i in range(n):
#         if A[i] > (maxSoFar + A[i]):
#             start = i
#             maxSoFar = A[i]
#         else:
#             maxSoFar = maxSoFar + A[i]
#
#         if maxSoFar > maxSum:
#             maxSum = maxSoFar
#             end = i
#
#     return (start, end)
#
#
# A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# (start, end) = DPFindMaxSubArray(A)
# print(A[start: end + 1])
