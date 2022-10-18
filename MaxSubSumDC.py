# A Divide and Conquer based program
# for maximum subarray sum problem

# Find the maximum possible sum in
# arr[] auch that arr[m] is part of it


def maxCrossingSum(arr, l, m, h):
    # Include elements on left of mid.
    sm = 0
    left_sum = -10000

    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if (sm > left_sum):
            left_sum = sm

    # Include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if (sm > right_sum):
            right_sum = sm

    # Return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2, 1]
    return max(left_sum + right_sum, left_sum, right_sum)


# Returns sum of maximum sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h):
    if (l == h):
        return arr[l]

    m = (l + h) // 2

    left_array = maxSubArraySum(arr, l, m)
    r_array = maxSubArraySum(arr, m + 1, h)

    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m + 1, h),
               maxCrossingSum(arr, l, m, h))


# Driver Code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)

max_sum = maxSubArraySum(arr, 0, n - 1)
print("Maximum contiguous sum is ", max_sum)
