class Solution(object):
    def wordPattern(self, pattern, s):
        lists = s.split()
        if len(pattern) != len(lists):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in dict1:
                dict1[pattern[i]] = lists[i]
            if lists[i] not in dict2:
                dict2[lists[i]] = pattern[i]
            if dict1[pattern[i]] != lists[i] or dict2[lists[i]] != pattern[i]:  # if the value of the key is not equal to the value of the key in the other dictionary then return False # revision needed
                return False
        return True

a1 = Solution()
print(a1.wordPattern('aabc','dog dog cat dog'))