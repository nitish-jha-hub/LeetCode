class Solution(object):
    def moveZeroes(self, nums):
        p = 0
        for x in range(len(nums)):
            if nums[x] !=0:
                temp = nums[p]
                nums[p] = nums[x]
                nums[x] = temp
                p+=1
        print(nums)
