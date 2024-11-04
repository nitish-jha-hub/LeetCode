class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # width = 0
        # height1 = 0
        maxwater =0
        start =0 
        end = len(height)-1
        while(start<end):
            water = min(height[start], height[end]) * ((end - start))
            if water>maxwater:
                maxwater = water
            if height[start] < height[end]:
                start +=1
            else:
                end -= 1
        return maxwater
        