nums = [1,3,5,6]
target = 5

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        midelement = nums[int((len(nums))/2)]
        if target == midelement:
            return int((len(nums))/2)
        elif target < midelement:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
                elif target < nums[i]:
                    return i

a = Solution()
k=a.searchInsert(nums, target)
print(k)

# practice