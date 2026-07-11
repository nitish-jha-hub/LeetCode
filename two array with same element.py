class Solution:
    def isIdentical(self, arrayx, arrayy):
        if len(arrayx) != len(arrayy):
            return False
        dict1 = {}
        for num in arrayx:
            if num not in dict1:
                dict1[num]=1
            else:
                dict1[num] += 1
        for num1 in arrayy:
            if num1 not in dict1 or dict1[num1] == 0:
                return False
            else:
                dict1[num1] -= 1

        return True
        



solobj = Solution()
ans = solobj.isIdentical([0,1,5,9], [1,5,9,0])
print(ans)