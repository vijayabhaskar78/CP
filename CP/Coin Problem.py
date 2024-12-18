def min_coins(V, coins):
    coins.sort(reverse=True)  # Sort coins in descending order
    result, count = [], 0

    for coin in coins:
        while V >= coin:
            V -= coin
            result.append(coin)
            count += 1

    if V != 0:
        return -1
    else:
        print("Coins:", result)
        print("Minimum coins needed:", count)
        return count

# Input and output handling
T = int(input())
for _ in range(T):
    V, N = map(int, input().split())
    coins = list(map(int, input().split()))
    min_coins(V, coins)