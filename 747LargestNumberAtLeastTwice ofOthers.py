class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = -1
        snum = -1
        nindex = 0
        # calculate the largest and second largest numbers and their index in o(n) time complexity 
        for i in range(len(nums)):
            if num<=nums[i]:
                snum = num
                num = nums[i]
                nindex = i
            elif snum <= nums[i]:
                snum = nums[i]
        if num >= snum*2:
            return nindex
        else:
            return -1