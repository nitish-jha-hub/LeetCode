#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        
        for i in range(len(arr)):
            sum=arr[i]
            if sum==target:
                return [i+1, i+1]
            for j in range(i+1,len(arr)):
                sum+=arr[j]
                if sum == target:
                    return [i+1,j+1]
        return [-1]
#  time complexity error
#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        curr_sum = 0
        start = 0
        for end in range(len(arr)):
            curr_sum += arr[end]
            
            while curr_sum > target and start <= end:
                curr_sum -=arr[start]
                start+=1
            
            if curr_sum == target:
                return [start+1, end+1]
        return [-1]
            