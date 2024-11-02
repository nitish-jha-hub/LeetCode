class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # test case pass but time limit exceed in 36th test case we have to done in O(n) not o(n^3)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i] < nums[j] <nums[k]:
        #                 return True
        # else:
        #     return False

            # O(n) solution Trick
        first = float('inf')
        second = float('inf')
        third = float('inf')
        for i in range(len(nums)):
        #    print(first,second,third)
           if first >= nums[i]:
                first = nums[i]
           elif second >= nums[i]:
                second = nums[i]
           else:
                third = nums[i]
                # print(first,second,third)
                return True
        else:
            return False