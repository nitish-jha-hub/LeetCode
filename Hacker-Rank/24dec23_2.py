def consecutivefinder(N, arr):
    arr.sort()

    for i in range(1, N):
        if arr[i] != arr[i - 1] + 1:
            return 0

    return 1  

# firstly we will take  Input
N = int(input())
arr = list(map(int, input().split()))

# Check with passing input to func and print Output
result = consecutivefinder(N, arr)
print(result)
