def uniqueId( arr):
        #  code here
        # set_arr = set(arr)  // error : because set in unordered collection of data but i need order maintain
        # new_list = list(set_arr)
        # new_list.sort()
        # return new_list
        new_list = []  
        for num in arr:
            if num not in new_list:
                new_list.append(num)
        return new_list
print(uniqueId([8,7,6,5,4]))