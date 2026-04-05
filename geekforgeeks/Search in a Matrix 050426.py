# Search in a Matrix
#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
    	# code here 
    # 	print(matrix)
    	for i in range(len(matrix)):
    	   for j in range(len(matrix[i])):
    	       if matrix[i][j] == x:
    	           return True
    	return False


# ! there is no arr.include so we use if x in arr:  in py
#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
    	# code here 
    # 	print(matrix)
    	for i in range(len(matrix)):
    	   #for j in range(len(matrix[i])):
    	   #    if matrix[i][j] == x:
    	   #        return True
    	   if x in matrix[i]:
    	       return True
    	
    	return False
