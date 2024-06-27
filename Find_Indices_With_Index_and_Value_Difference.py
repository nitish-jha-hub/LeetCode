class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j]) >= valueDifference and abs(i-j) >= indexDifference:
                    return [i,j]
        return [-1,-1]

        