first_no = int('671')
second_no = int('329')

digits_array1 = [int(digit) for digit in str(first_no)]
digits_array2 = [int(digit) for digit in str(second_no)]


carry_digit = 0

if len(digits_array1)<=len(digits_array2):
    carry = 0
    for i in range(len(digits_array1)):
        # print(i)
        if (digits_array1[-(1+i)]+digits_array2[-(1+i)] +carry) >9 :  
            print(digits_array1[-(1+i)],digits_array2[-(1+i)])          
            carry+=1
            carry_digit+=1
        else:
            carry =0
                   

print(carry_digit)