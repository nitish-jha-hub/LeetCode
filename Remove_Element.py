a= [0,1,2,2,3,0,2,4,2,2]
val = 2
# for i in range(len(a)):
#     try:
#         if a[i] == val:
#             a.pop(i)
#             a.append(0)
#     except Exception as e:
#         print(e)
#         continue
# print(a)

# def removeElement(nums, val):
#         for num in nums:
#             print(num, sep=' ', end=' ', flush=True)
#             if num == val:
#                 nums.remove(num)
#         return nums

# print(removeElement(a,val))

class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
                nums.remove(val)
        return len(nums)