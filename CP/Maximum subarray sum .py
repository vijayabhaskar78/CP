def max_subarray_sum_cubic(arr):
    n = len(arr)
    max_sum = float('-inf')
    
    # Try all possible subarrays
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            # Calculate sum of current subarray
            for k in range(i, j + 1):
                current_sum += arr[k]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_sum_quadratic(arr):
    n = len(arr)
    max_sum = float('-inf')
    
    # Try all possible subarrays
    for i in range(n):
        current_sum = 0
        # Calculate sum for subarrays starting at i
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_sum_linear(arr):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        # Either start a new subarray or extend the existing one
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Brute Force (O(n³)) solution:", max_subarray_sum_cubic(arr))
print("Quadratic (O(n²)) solution:", max_subarray_sum_quadratic(arr))
print("Kadane's Algorithm (O(n)) solution:", max_subarray_sum_linear(arr))