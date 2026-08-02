class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arrays = []
        level=0
        for char in s:
            if char == '(' and level > 0:
                print(arrays)
                arrays.append(char)
                level +=1
            elif char == ')' and level > 1:
                arrays.append(char)
                level -=1
            elif char == '(':
                level+=1
            elif char == ')':
                level-=1
        return "".join(arrays)
                        
        print(arrays)

print(Solution().removeOuterParentheses("(()())(())(()(()))"))
        