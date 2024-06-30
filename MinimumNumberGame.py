class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(int(len(nums)/2)):
            alice = min(*nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            # print(nums)
            arr.append(bob)
            arr.append(alice)
        return (arr)
        