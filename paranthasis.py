class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack1 = []
        inp = ['[','{','(']
        outp = [']','}',')']
        for i in range(len(s)):
            if s[i] in inp:
                stack1.append(s[i])
            elif s[i] in outp:
                if len(stack1) == 0:
                    return False
                if inp.index(stack1[-1]) == outp.index(s[i]):   # check if the last element in stack is the corresponding opening bracket for the closing bracket # remember to use index to get the index of the element in the list
                    stack1.pop()
                else:
                    return False
        if len(stack1) == 0:
            return True