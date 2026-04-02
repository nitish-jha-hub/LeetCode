arr = [16,17,5,2]

# class Solution:
#     def leaders(self, arr):
#         # code here
#         output_arr = []
#         # output_arr = [arr[len(arr)-1]] if arr else []
#         for i in range(len(arr)-1):
#             max_ele = max(arr[i:len(arr)-1])
#             if max_ele == arr[i]:
#                 output_arr.append(arr[i])
#             # print(i)
#             # return
#         return output_arr.append(arr[len(arr)-1])

class Solution:
    def leaders(self, arr):
        # code here
        output_arr = []
        max_ele = arr[len(arr)-1]
        output_arr.append(max_ele)
        for i in range(len(arr)-2, -1, -1):
            if arr[i] >= max_ele:
                output_arr.append(arr[i])
                max_ele = arr[i]
        return output_arr[::-1]
sol = Solution()
print(sol.leaders(arr))