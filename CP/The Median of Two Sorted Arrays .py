def find_median(arr1, arr2):
    merged = sorted(arr1 + arr2)
    mid = len(merged) // 2
    return (merged[mid] + merged[~mid]) / 2

# Input and output
n1, n2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(find_median(arr1, arr2))