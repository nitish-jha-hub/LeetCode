# class Solution:
# 	def minJumps(self, arr):
# 	    # code here
# 	    no_of_jump = 0
# 	    current_position = 0
# 	    target = len(arr)
# 	   # for i in range(len(arr)):
# 	   #     print(i)
# 	   #     max_jump = max(arr[arr[i]:arr[i+arr[i]]])
# 	   #     i+=max_jump
# 	   #     no_of_jump +=1
# 	   #     if i>len(arr):
# 	   #         return no_of_jump
	   
#     	while current_position <= target :
    	       
#     	       max_jump = max(arr[current_position : current_position+arr[current_position]])
    	       
#     	       current_position = current_position + max_jump
#     	       no_of_jump+=1
#     	       if current_position <= target and arr[current_position] == 0:
# 	                return -1
#     	return(no_of_jump)
    	       
	       
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # Edge cases
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 1
        max_reach = arr[0]
        steps = arr[0]
        
        for i in range(1, n):
            
            # If we reached end
            if i == n - 1:
                return jumps
            
            # Update max reach
            max_reach = max(max_reach, i + arr[i])
            
            # Use a step
            steps -= 1
            
            # If no steps left
            if steps == 0:
                jumps += 1
                
                # If current index >= max reach → stuck
                if i >= max_reach:
                    return -1
                
                # Reset steps
                steps = max_reach - i
        
        return -1