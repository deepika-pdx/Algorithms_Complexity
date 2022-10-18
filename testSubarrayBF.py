def test(nums):
    n = len(nums)
    maximumSubArraySum = 0
    start = 0;
    end = 0;

    for left in range(n):

        runningWindowSum = 0

        for right in range(left, n):
            runningWindowSum = runningWindowSum + nums[right]

            if runningWindowSum > maximumSubArraySum:
                maximumSubArraySum = runningWindowSum
                start = left
                end = right
    return (start, end)


A = [-3, 6, 8, -3, -10, 13]
(start, end) = test(A)
print(A[start:end + 1])
