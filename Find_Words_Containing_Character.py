class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        arr = []
        for word in enumerate(words):
            if x in word[1]:
                arr.append(word[0])
        return arr
                