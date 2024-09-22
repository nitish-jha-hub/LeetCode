nums = [1,1,1,2,2,2,3]

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import collections
        freq = collections.Counter(nums)
        freqdict = dict(freq)
        soertedfreq = sorted(freqdict.values())
        print(soertedfreq)
        res = [freqdict[x] for x in soertedfreq]
        print (res)


a = Solution()
a.frequencySort(nums)
