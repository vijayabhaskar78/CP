#Euclid Problem  

def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, d = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return x, y, d

# Single input processing
a, b = map(int, input().split())
x, y, d = extended_gcd(a, b)
if x > y:
    x, y = y, x
print(x, y, d)