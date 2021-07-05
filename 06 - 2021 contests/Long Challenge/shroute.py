t = int(input())
for q in range(0, t):
    N, M = map(int ,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ans = [None] * N
    ans[0] = 0
    maximum_value = 10 ** 9
    
    for i in range(0, N):
        
        if (i == 0) or (A[i] != 0):
            ans[i] = 0
        else:
            ans[i] = maximum_value
            
    high = -1
    
    for j in range(0, N):
        if (A[j] == 1):
            high = j
        if (high != -1):
            if (A[j] == 0):
                ans[j] = min(ans[j], j - high)
    
    low = -1
    
    for k in range(N - 1, -1, -1):
        if (A[k] == 2):
            low = k
        if (low != -1):
            if (A[k] == 0):
                ans[k] = min(ans[k], low - k)
                
    for l in range(0, M):
        temp = B[l] - 1
        
        if (ans[temp] != maximum_value):
            print(ans[temp], end = " ")
        else:
            print(-1, end = " ")
            
    print()

