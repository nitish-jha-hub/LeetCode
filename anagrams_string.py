def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


#Rough
# print(is_anagram("abgc", "cgba"),sorted("nitish")) # True

# print([1,2,3,4,5,6,7,8,9,10][::2])

# print([1,2,3,48] == [1,2,3,48]) # in js it will return false because of reference but in python it will return true because of value comparison