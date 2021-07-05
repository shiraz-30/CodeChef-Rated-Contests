t = int(input())
for i in range(0, t):
    D, d, p, q = map(int, input().split())
    
    x = (D //d)
    ans = (d * x * p) + ((q * (x - 1) * (x) * d) // 2)
    
    if (D % d == 0):
        print(ans)
    
    else:
        y = (D % d)
        ans += (y * (p + (x * q)))
        print(ans)

