t = int(input())
for i in range(0, t):
    a, b, c, d, k = map(int, input().split())
    
    x = abs(c - a) + abs(d - b)
    y = k - x
    
    if (y % 2 == 0 and k >= x):
        print("YES")
    else:
        print("NO")

