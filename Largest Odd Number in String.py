class Solution:
    def largestOddNumber(self, num: str) -> str:
        # print(int(num))
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) %2 != 0:
                # print(num[i],i,type(num))
                return num[0:i+1]
        return ""



print(Solution().largestOddNumber("545426"))