def fibonaci_series(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            if c > 100:
                break
            print(c)
# fibonaci_series(101)

# print the fibonaci series upto 100
def fibonaci_series2(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        while True:
            c = a + b
            a = b
            b = c
            if c >= n:
                break
            print(c)
fibonaci_series2(14)            