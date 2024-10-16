n=0
if n == 0:
    print(False)
for factor in [2, 3, 5]:
    while n % factor == 0:
        print(n)
        n //= factor
print(n == 1)

# for factor in [2,3,5]:
#     while n%factor == 0:
#         n = n // factor
#         if n==1:
#             print(True)
# else:
#     print(False)