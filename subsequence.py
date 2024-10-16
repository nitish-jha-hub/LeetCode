# revision needed
# Consider the function f defined here, for a given linked list p, the function f returns 1 if and only if ______
# def longest_decreasing_subsequence(seq):
#     n = len(seq)
#     # Initialize a list to store the length of the longest decreasing subsequence ending at each index
#     lds = [1] * n
    
#     # Compute the length of the longest decreasing subsequence
#     for i in range(1, n):
#         for j in range(0, i):
#             if seq[i] < seq[j] and lds[i] < lds[j] + 1:
#                 lds[i] = lds[j] + 1
                
#     # Find the maximum length in lds
#     max_length = max(lds)
    
#     # Reconstruct the longest decreasing subsequence
#     lds_seq = []
#     for i in reversed(range(n)):
#         if lds[i] == max_length:
#             lds_seq.append(seq[i])
#             max_length -= 1
    
#     return lds_seq

# # Example usage
# sequence = [5, 3, 4, 8, 6, 7, 1, 2]
# print("Longest Decreasing Subsequence:", longest_decreasing_subsequence(sequence))

# Input 2 :1056378914121315Output 2 :2

def longest_decreasing_subsequence(seq):
    n = len(seq)
    lds = [1] * n
    
    for i in range(1, n):
        for j in range(0, i):
            if seq[i] < seq[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
                
    max_length = max(lds)
    return max_length

def main():
    # Input the sequence as a single string and convert to list of integers
    seq = list(map(int, "1056378914121315"))
    
    # Find the length of the longest decreasing subsequence
    result = longest_decreasing_subsequence(seq)
    
    print("Longest Decreasing Subsequence Length:", result)

if __name__ == "__main__":
    main()
