class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1= {}
        for i in range(len(s)):
            if s[i] in dict1:
                if dict1[s[i]] == t[i]:
                    # print(dict1)
                    continue
                else:
                    return False
            else:
                if t[i] in dict1.values():
                    return False
                else:
                    dict1[s[i]] = t[i]
        print(dict1)
        return True

        

print(Solution().isIsomorphic("badc", "baba"))