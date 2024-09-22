s ="a good   example"

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        arr = s.split(" ")
        arr = [x.strip() for x in arr if x != '']
        arrrev = arr[::-1]
        arrfinal = " ".join(arrrev)
        return arrfinal
        
a = Solution()
print(a.reverseWords(s))
        