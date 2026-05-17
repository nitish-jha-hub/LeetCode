def rotate(arr):
    last = arr.pop()
    arr.insert(0,last)
    return arr
print(rotate ([3,4,5]))