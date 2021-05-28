t = int(input())
for i in range(0, t):
    N, M = map(int, input().split())
    
    arr = map(int, input().split())
    x = set(arr)
        
    if (len(x) < M):
        print("Yes")
    else:
        print("No")
        
        
    
    