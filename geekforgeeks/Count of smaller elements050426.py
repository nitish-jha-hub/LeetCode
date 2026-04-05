# Count of smaller elements
#User function Template for python3

class Solution:
    def countOfElements(self, x, arr):
        # Code Here
        count = 0
        for i in range(len(arr)):
            if arr[i] <= x :
                count +=1
        return count

