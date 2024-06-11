a = [1,2,3,0,0,0]
m= 3
b = [2,5,6]
n = 3
def merge(a,m,b,n):
    a[m:] = b
    a.sort()
    return a

print(merge(a,m,b,n))