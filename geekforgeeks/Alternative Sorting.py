# class Solution:
#     def alternateSort(self,arr):
#         # Your code goes here
#         arr1 =[]
#         while len(arr) :
#             maxele = max(arr)
#             arr1.append(maxele)
#             arr.remove(maxele)
#             if len(arr):

#                 minele = min(arr)
#                 arr1.append(minele)
#                 arr.remove(minele)
#         return arr1
# sol = Solution().alternateSort([7, 1, 2, 3, 4, 5,6])
# print(sol)


def alternateSort(self, arr):
    arr.sort()
    l, r = 0, len(arr) - 1
    arr1 = []
    while l <= r:
        arr1.append(arr[r])
        r -= 1
        if l <= r:
            arr1.append(arr[l])
            l += 1
    return arr1
