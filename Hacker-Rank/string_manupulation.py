string = "rererere"
position = 5
character = 'c'
def mutate_string(string, position, character):
    a = string
    b = list(a)
    b[position] = character
    d = ''.join(b)
    return d

print(mutate_string(string, position, character))