# done both public and private
def nitishtoggle(valid_digits, fd):   
    pd = []
    for digit, valid in valid_digits.items():     
        diff = sum(1 for a, b in zip(fd, valid) if a != b)
        if diff == 0:
            pd.append(digit)
        elif diff == 1:  
            pd.append(digit)
    return pd

def solve():    
    sd = [input().strip() for _ in range(3)]  

    fad = [input().strip() for _ in range(3)]   
   
    valid_digits = {}
    for i in range(10):
        valid_digits[i] = ''.join(sd[j][i*3:(i+1)*3] for j in range(3))   
   
    faulty_number = []
    for i in range(len(fad[0]) // 3):
        fd = ''.join(fad[j][i*3:(i+1)*3] for j in range(3))
        pd = nitishtoggle(valid_digits, fd)
        if not pd:
            print("Invalid",end='')
            return
        faulty_number.append(pd) 

    from itertools import product
    ts = 0
    for possible in product(*faulty_number):
        ts += int(''.join(map(str, possible)))    
    print(ts,end='')
solve()

Toggle Challenge
Problem Description
Deepika has a challenge for you involving a seven-segment display! Let us see what it is.

Deepika will provide you with the 7-segment display of digits from 0 to 9, each represented in a 3x3 matrix format, all arranged in 3 lines. (Refer input format)

Now, she will present you with a 7-segment display of a number that may be having some faults in it. You are allowed to toggle (LED light either on or off where 0 is off and 1 is on, which again will be turned back to original state) at most one light for each digit at a time, to form new numbers. Print the sum of all the numbers that can be formed.

Constraints
1 <= number of digits in the input number <= 50

Given input number will not start with 0.

All the numbers from 0-9 will be unique in 7-segment display.

Input
The first three lines will contain the 3x3 matrix representations (7-segment display) of the digits from 0 to 9. In other words, first three lines consists of a 3*9 matrix consisting of only 1 and 0, where 1 indicates that the LED light is on and 0 means it is off.

The next three lines will show the 7-segment display of the number provided by Deepika.

Output
Print the sum of all the numbers that can be formed by toggling the LED lights. If there is any digit in the input number that is invalid and cannot become a valid digit by toggling one light on or off, print "Invalid"

Time Limit (secs)
1

Examples
Example 1

Input

111001111111101111111111111111

101001001011111010100001111111

111001111111001111111001111001

001111111111

000001111010

001011111111

Output

17888

Explanation

The first 3 lines, each having 30 columns represent numbers from 0 to 9. Each 3x3 matrix denoted in either red or green, represents individual numbers. The only purpose of colouring is readability.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@7d373bcf:image1.png

Next 3 lines of the input denote the actual LEDs which are to be toggled to solve the actual problem mentioned in description section above.


Let us number the 9 lights present in each matrix from 1-9. Below are the few possibilities -

1. Toggle 6th light in first 3*3 matrix, 7th light in second 3*3 matrix. Keep the rest same. Number formed will be 1285. Reset the lights to original.

2. Toggle 6th light in first 3*3 matrix, 7th light in second 3*3 matrix, 5th light in the third 3*3 matrix and keep the rest same. Number formed will be 1205. Reset the lights to original.

3. Toggle 6th light in first 3*3 matrix, 7th light in second 3*3 matrix, 4th light in the third 3*3 matrix and keep the rest same. Number formed will be 1235. Reset the lights to original.

4. Toggle 6th light in first 3*3 matrix, 7th light in second 3*3 matrix, 4th light in the third 3*3 matrix and 6th light in the fourth 3*3 matrix. Keep the rest same. Number formed will be 1233. Reset the lights to original.

...

..

All the numbers we can form is {1203, 1205, 1233, 1235, 1283, 1285, 1703, 1705, 1733, 1735, 1783, 1785} and their sum is 17888. Hence print the same.

Example 2

Input

111001111111101010111111111111

101001100011111111001001111111

111001111111001010111001111001

010111111100

111101011100

010111110100

Output

Invalid

Explanation

The first 3 lines, each having 30 columns represent numbers from 0 to 9. Each 3x3 matrix denoted in either red or green, represents individual numbers. The only purpose of colouring is readability.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@7d373bcf:image2.png

Next 3 lines of the input denote the actual LEDs which are to be toggled to solve the actual problem mentioned in description section above.

Consider the last 3*3 matrix on lines 4 - 6, which is

100

100

100

Based on the provided seven-segment display for the digits 0 to 9, this digit (matrix) is faulty and cannot be corrected by toggling a single light. Therefore, print "Invalid"