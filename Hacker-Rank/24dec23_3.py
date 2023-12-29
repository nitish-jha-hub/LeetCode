def removegtop(input_str):
    result = input_str[0]
    
    for char in input_str[1:]:
        if char == '+' and result[-1] == '+':
            continue
        result += char   
    return result
input_str = input()
output_str = removegtop(input_str)
print(output_str)