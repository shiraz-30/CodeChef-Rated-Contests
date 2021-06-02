# Partially Correct [20 pts]

def taking_gcd_adjacently(a, b):
    if b == 0:
        return a
    return math.gcd(b, a % b)


import math
t = int(input())
for i in range(0, t):
    k = int(input())
    result = 0
    mod = 10**9 + 7
    
    for j in range(1, 2*k + 1):
        result += taking_gcd_adjacently(k + j* j, k + (j+1) * (j + 1))
        
    print(result % mod)

        
        