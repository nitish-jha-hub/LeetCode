class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # n = 2**len(nums)
        # print(n)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         print(nums[i], nums[j])
        subsets = [[]]
        for element in nums:
            print(element)
            subsets += [(current + [element]) for current in subsets]
            print(subsets)
        return subsets