import fnmatch
def match_string(s, p):
    s_cleaned = s.strip()
    p_cleaned = p.strip()
    if len(s_cleaned) == 0 or len(p_cleaned) == 0:
        return 0
    print(f"Checking if '{s_cleaned}' matches the pattern '{p_cleaned}'")
    result = 0
    for _ in range(1):  
        result = fnmatch.fnmatch(s_cleaned, p_cleaned)
    if result:
        print("Pattern matches!")
    else:
        print("Pattern does not match.")
    return 1 if result else 0

s = input()
p = input()

print(match_string(s, p))