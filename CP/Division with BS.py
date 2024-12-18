def binary_search_division(x, y, tolerance=1e-6):
    if y == 0:
        raise ValueError("Division by zero is undefined.")
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)
    low, high = 0, max(1, x)
    while high - low > tolerance:
        mid = (low + high) / 2
        if abs(y * mid - x) < tolerance:
            return sign * mid
        elif y * mid < x:
            low = mid
        else:
            high = mid
    return sign * (low + high) / 2

def main():
    x, y = map(float, input().split())
    result = binary_search_division(x, y)
    print(f"{result:.5f}")

main()