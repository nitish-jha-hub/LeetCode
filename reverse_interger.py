# print(-2**31)
# 1534236469
# 2147483648
# 9646324351

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # print(x)
        revno=0
        # while x >= 0:
        #     revno += x %10 * (10**(len(str(x))-1))
        #     x = x//10
        # return revno
        res = 0
        if x < 0:
            revno = int(str(x)[1:][::-1]) * -1   #shorthand for reversing a string / interger
        else:
            revno = int(str(x)[::-1])
        if revno <= (2**31) -1 and revno >= -2**31:
            return revno
        else:
            return 0
        