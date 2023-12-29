
from pickle import FALSE


def isPalindrome(x):
    y = str(x)

    if y[0] == '-':
        y = y[1:]
        return False
    else:
        # print(y,len(y))
        for i in range(len(y)):
            print(i)
            if y[i] != y[len(y)-(i+1)]:
                return False
        return True



print(isPalindrome(121))
