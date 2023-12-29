def process_arrays(N, A, B):
    result = []

    for i in range(N):
        if ( 10<=A[i]<100 and A[i] % 2 )== 1 and B[i] % 2 == 0:
            result.append(A[i] + B[i])
        elif A[i] % 2 == 0 and B[i] % 2 == 1:
            result.append(A[i] - B[i])
        elif A[i] % 2 == 0 and B[i] % 2 == 0:
            result.append(A[i] * B[i])
        elif A[i] % 2 == 1 and B[i] % 2 == 1:
            result.append(A[i] * B[i])
        else:
            result.append(0)

    print('\n'.join(map(str, result)))

# Sample Input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Process and Output
process_arrays(N, A, B)



