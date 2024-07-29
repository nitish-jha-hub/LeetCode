nums =[1,2,1]


class Solution(object):
    def getConcatenation(self, nums):
        print([*nums, *nums])
        nums = nums

a =Solution()
a.getConcatenation(nums)

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=nums+nums
        return nums
        # print([*nums, *nums])  don't know why it is not working in leetcode interpreter