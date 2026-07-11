class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2= ""
        for word in word1:
            str1 +=word
        for wordy in word2:
            str2 += wordy
        return str1 == str2
        


print(Solution().arrayStringsAreEqual(["ab", ""], ["a", "bc"]))