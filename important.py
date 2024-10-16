from math import trunc

# create a list with 5 elements, all of them equal to 1
list1 = [1] * 5
# print(list1)

# trunc function from the math module
truncate1 = trunc(3.14159) # `trunc` is a function from the `math` module that truncates a number to its integer part

# enumerate function
# for i,value in enumerate(list1):
    # print(i,value)

subsets = [[]]
list2 = [1,2,3]
for element in list2:
    subsets += [[element]+ current for current in subsets] 
    print(subsets)