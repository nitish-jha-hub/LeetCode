# run on python3 on leetcode but not on python: Maybe leetcode problem 
nums1 = [1,2]
nums2 = [3,4]


# num3 = (nums1 + nums2)
# num3.sort()
# median = 0
# if len(num3) % 2 == 0:
#     median = (num3[int(len(num3)/2)] + num3[int(len(num3)/2) - 1]) / 2
# else:
#     median = num3[int(len(num3)/2)]
# print(median)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num3 = (nums1 + nums2)
        num3.sort()
        median = 0
        if len(num3) % 2 == 0:
            median = (num3[int(len(num3)/2)] + num3[int(len(num3)/2) - 1]) / 2
        else:
            median = num3[int(len(num3)/2)]
        return median
    
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
