t = int(input())
for i in range(0, t):
    M, S = map(int, input().split())
    x = M - S
    if x >= 0:
        y = x // S 
        z = y + 1
        
        print(z)
    
    else:
        print(0)
