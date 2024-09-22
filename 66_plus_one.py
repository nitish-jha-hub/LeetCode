class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        no = 0
        for i in range(len(digits)):
            print(i)
            no += digits[i] *10**(len(digits)-1-i)    # create number from list
        # print(no)
        no+=1
        # create new list of digits from number after adding 1
        newarr=[]
        while no >0:
            newarr.insert(0,no%10)  # insert at 0th index
            no= no //10
        return newarr

