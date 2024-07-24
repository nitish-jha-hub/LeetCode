class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(ord("h"))
        sum = 0
        for x in range(len(s)-1):
            sum += abs(ord(s[x]) -ord(s[x+1]))  # ord gives ascii value of a character and  abs gives absolute value
        return(sum)