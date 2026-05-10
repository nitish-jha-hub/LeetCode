class Solution:
    def coin(self, arr):
        # code here
        while len(arr) >1:
            first = arr[0]
            last = arr[-1]
            if first > last:
                # arr.remove(first)   // !nitish memory limit error but pop work means pop usage low memory
                arr.pop(0)
            else:
                # arr.remove(last)
                arr.pop()
            
        return arr[0]

# result = Solution().coin([5, 3, 1, 6, 9])

# print(result)

result = Solution().coin([5, 3, 1, 6, 9])

print(result)