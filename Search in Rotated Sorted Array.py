# this is brute force method optimul solution is o(log n) by binary search
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#         return -1

#binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <=high :
            mid = (low + high) //2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[low] <= nums [mid]:
                if target >= nums[low] and target<= nums[mid]:
                    high= mid-1
                else:
                    low = mid+1
            else:
                if target >= nums[mid] and target <=nums[high]:
                    low = mid+1
                else:   
                    high = mid -1
        return -1

print(Solution().search([4,5,6,7,0,1,2],0))