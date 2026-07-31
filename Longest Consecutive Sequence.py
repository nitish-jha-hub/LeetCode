class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        maxcount=1
        count1=1
        if len(nums) ==0:
            return 0
        if len(nums) ==1:
            return 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] +1 == nums[i+1] :
                count1+=1
            else:
                count1= 1
            if count1 > maxcount:
                print(count1, maxcount)
                maxcount = count1

        return maxcount