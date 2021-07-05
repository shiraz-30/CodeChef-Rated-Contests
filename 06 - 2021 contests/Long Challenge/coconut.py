t = int(input())
for i in range(0, t):
    x_a, x_b, X_a, X_b = map(int, input().split())
    
    p = (X_a // x_a)
    q = (X_b // x_b)
    
    print(p + q)
    
