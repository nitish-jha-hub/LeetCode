class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        def backtrack(combination):
            if len(combination) == len(nums):
                # create copy of the combination bfr add it to results
                results.append(combination[:])
                return

            for num in nums:
                if num not in combination:
                    combination.append(num)
                    backtrack(combination)
                    combination.pop()

        backtrack([])
        return results
        