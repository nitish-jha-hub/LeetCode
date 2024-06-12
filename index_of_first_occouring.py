class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            a = haystack.index(needle,0)
            return a
        else:
            return -1

        