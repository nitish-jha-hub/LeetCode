class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        mon=n/7
        rem_d=n%7
        return(7*mon*(mon+7)/2+rem_d*mon+rem_d*(rem_d+1)/2)

c= Solution()
print(c.totalMoney(10))