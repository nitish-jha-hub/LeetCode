class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative = []
        res =[0] * len(nums)
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        for i in range(len(nums)//2):
            print(f"ijkkj {i}")
            res[2 * i] = positive[i]
            res [2 * i +1] = negative[i]

        return res

print(Solution().rearrangeArray([3,1,-2,-5,2,-4]))