# def removeDuplicates():
#     num =[0,0,1,1,1,3,3,5,5]
#     a=set(num)
#     b=list(a)
#     print(len(b))
#     for i in range(len(b)):
#         print(b[i])

# removeDuplicates()

def removeDuplicates(nums):
    i=0
    j=1
    while i<=j and j<len(nums):
        if nums[i]==nums[j]:
            j+=1
        else:
            nums[i+1]=nums[j]
            i+=1
    return i+1            