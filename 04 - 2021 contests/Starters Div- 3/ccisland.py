t = int(input())
for i in range(0, t):
    x, y, xr, yr, D = map(int, input().split())
    
    a = x / xr 
    b = y / yr
    c = min(a, b)
    
    if (c >= D):
        print("YES")
    else:
        print("NO")
        
        
