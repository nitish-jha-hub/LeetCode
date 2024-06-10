s = ["h","e","l","l","o","w","o","r","l","d"]

for i in range(len(s)//2):
    s[i], s[-i-1] = s[-i-1], s[i]   # swapping the elements of the list in reverse order 

print(s)