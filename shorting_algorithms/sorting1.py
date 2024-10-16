listex = [7,8,1,2,3,545454,454,5,5,5,4,54,54,54,54,56,77,6,8,7,78,78,78,78,78,5,4]

# build-in list sort method
# listex.sort()
# print(listex)

import time

# bubble sort
start1 = time.time()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(listex))
endb = time.time()
print(endb - start1)

# selection sort
start2 = time.time()
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort(listex))
end2= time.time()
print(end2 - start2)

# insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort(listex))

# merge sort
def merge_sort(arr):
    pass