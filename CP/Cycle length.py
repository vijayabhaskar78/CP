def cycle_length(n):
    count = 1
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count
i, j = map(int, input().split())
print(i, j, max(cycle_length(n) for n in range(min(i, j), max(i, j) + 1)))