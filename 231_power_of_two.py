class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(32):
            if pow(2,i) == n:
                return True
        return False
        