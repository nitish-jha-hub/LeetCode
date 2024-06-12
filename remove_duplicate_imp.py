class Solution(object):
    def findDuplicate(self, nums):
        while nums[0] != nums[nums[0]]:
            nums[nums[0]],nums[0] = nums[0],nums[nums[0]]
        return nums[0]