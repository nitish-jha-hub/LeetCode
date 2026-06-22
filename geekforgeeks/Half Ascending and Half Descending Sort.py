class Solution:
    def customSort(self, arr):
        # code here
        # arr.sort()
        # firsthalf = arr[0:len(arr)/2]
        length1 = (len(arr) //2)
        arr1 = arr[0:length1]
        arr1.sort()
        arr2 = arr [length1:len(arr)]  
        arr2.sort()
        revarr2 = arr2[::-1]
        return [*arr1, *revarr2]

print(Solution().customSort([10, 20, 30, 40]))