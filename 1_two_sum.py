nums = [5,6,9,8,4,3]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[j] == target - nums[i]:
#             print([i,j])
          
Solution.twoSum()

