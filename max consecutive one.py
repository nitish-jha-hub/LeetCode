class Solution:
    def nitish(self, arrx):
        lastmax=0
        currentmax=0
        for num in arrx:
            if num ==1:
                currentmax +=1
            if num != 1 and currentmax > lastmax:

                lastmax = currentmax
            if  num != 1:
                # print(currentmax)
                currentmax = 0
            
        return lastmax if lastmax > currentmax else currentmax


print(Solution().nitish([1,0,1,1,0,1]))