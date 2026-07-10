class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        last = len(nums) - 1
        while(start <= last):
            mid = (start + last) //2
            if (nums[mid] == target):
                return mid
            elif (target > nums[mid]):
                start = mid +1
            elif (target < nums[mid]):
                last = mid-1
        else:
            return -1
newobjx = Solution()
ans = newobjx.search([-1,0,3,5,9,12], 9)
print(ans)