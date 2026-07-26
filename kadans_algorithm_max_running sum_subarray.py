class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        maxsum=nums[0]
        runningsum=0
        for num in nums:
            # print(num)
            runningsum = runningsum + num
            if runningsum < 0:
                runningsum = 0
            elif runningsum>maxsum:
                maxsum = runningsum
            if num> maxsum:
                # print("eeeeeeeeeeeeeeee")
                maxsum = num
        return maxsum


        





print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))