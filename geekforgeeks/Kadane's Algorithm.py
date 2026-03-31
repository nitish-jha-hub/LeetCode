#max running sum in array with +ve and -ve numbers
# Kadane's Algorithm
class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        curr_sum = arr[0]
        max_sum = arr[0]
        for i in range(1,len(arr)):
            max_sum = max(arr[i], curr_sum + arr[i])
            curr_sum = max(max_sum, arr[i])
        return max_sum