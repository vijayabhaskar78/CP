def first_set_bit(N):
    # If N is 0, return 0 as no set bit exists
    if N == 0:
        return 0
    
    # Isolate the rightmost set bit and calculate its position
    return (N & -N).bit_length()


def first_set_bit(N):
    if N == 0:
        return 0
    position = 1  # Position of the first bit (starting from 1)
    while N > 0:
        if N & 1:  # Check if the current bit is set
            return position
        N >>= 1  # Right-shift N to check the next bit
        position += 1


"""Test case 1 
Input: N = 18 
Output: 2 
Test case 2 
Input: N = 12  
Output: 3  
Expected Time Complexity: O(log N)."""