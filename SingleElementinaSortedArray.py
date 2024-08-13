# Single Element in a Sorted Array
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: in
        """
        start = 0
        end = len(nums) - 1
        while start < end:             #BINARY SEARCH method
            # mid = start + (end - start) // 2
            mid = ((end + start) // 2)
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                start = mid + 2
            else:
                end = mid
        return nums[start]

nums = [1,1,2,3,3,8,8]
sol = Solution()
print(sol.singleNonDuplicate(nums))

# practice