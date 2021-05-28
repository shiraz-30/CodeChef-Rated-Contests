t = int(input())
for i in range(0, t):
    X, Y, Z, T, A, B, C = map(int, input().split())
    
    s = A + B + C 
    
    if (A >= X and B >= Y and C >= Z and s >= T):
        print("YES")
    else:
        print("NO")
        
    
    
