def parse_matrix(lines, start, end):
    """Extract a segment of lines and split into 3x3 matrices."""
    matrix = []
    for line in lines[start:end]:
        matrix.append([line[i:i+3] for i in range(0, len(line), 3)])
    return list(zip(*matrix))

def toggle_light(matrix):
    """Generate all possible matrices by toggling one light."""
    toggled = []
    for i in range(3):
        for j in range(3):
            new_matrix = [row[:] for row in matrix]
            new_matrix[i][j] = '1' if matrix[i][j] == '0' else '0'
            toggled.append(new_matrix)
    return toggled

def is_valid_digit(matrix, digit_map):
    """Check if a matrix is a valid digit or can be made valid."""
    str_matrix = ["".join(row) for row in matrix]
    if str_matrix in digit_map:
        return True, digit_map.index(str_matrix)
    
    # Try toggling one light
    for toggled in toggle_light(matrix):
        toggled_str = ["".join(row) for row in toggled]
        if toggled_str in digit_map:
            return True, digit_map.index(toggled_str)
    
    return False, None

def main():
    import sys
    input = sys.stdin.read().strip().split("\n")
    
    # First 3 lines: 7-segment display for digits 0-9
    digit_map = parse_matrix(input, 0, 3)
    digit_map = [["".join(row) for row in digit] for digit in digit_map]
    
    # Next 3 lines: Input number
    input_number = parse_matrix(input, 3, 6)
    input_number = [["".join(row) for row in digit] for digit in input_number]
    
    all_numbers = set()
    is_invalid = False

    # Process each digit
    for i, digit in enumerate(input_number):
        valid, base_digit = is_valid_digit(digit, digit_map)
        if not valid:
            is_invalid = True
            break
        
        # Generate all valid toggles
        current_variants = set()
        for toggled in toggle_light(digit):
            toggled_str = ["".join(row) for row in toggled]
            if toggled_str in digit_map:
                current_variants.add(digit_map.index(toggled_str))
        
        # Cross-multiply with existing numbers
        if i == 0:
            all_numbers = current_variants
        else:
            all_numbers = {num * 10 + var for num in all_numbers for var in current_variants}
    
    if is_invalid:
        print("Invalid")
    else:
        print(sum(all_numbers))
