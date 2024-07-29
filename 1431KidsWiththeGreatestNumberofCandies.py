extraCandies = 3
candies = [2,3,5,1,3]

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        candiesdup = [*candies]
        candiesdup.sort()
        max = candiesdup[-1]
        result = []
        for i in candies:
            if i + extraCandies >= max:
                result.append(True)
            else:
                result.append(False)
        print(result)
        return result


a = Solution()
a.kidsWithCandies(candies, extraCandies)