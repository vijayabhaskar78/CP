def find_max_triplet(arr):
    if len(arr) < 3:
        return "Array should have at least 3 elements"

    arr.sort()
    product1 = arr[-1] * arr[-2] * arr[-3]
    product2 = arr[0] * arr[1] * arr[-1]
    if product1 > product2:
        return arr[-1], arr[-2], arr[-3]
    else:
        return arr[0], arr[1], arr[-1]

n = int(input()) 
arr = list(map(int, input().split()))  
triplet = find_max_triplet(arr)
print(*triplet)

"""5
1  7  2  -2  5 
7 5 2"""