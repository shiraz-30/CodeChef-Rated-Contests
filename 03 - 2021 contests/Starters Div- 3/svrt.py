t = int(input())
for i in range(0, t):
    N, K = map(int, input().split())
    
    if ((N % K) == 0):
        D = (N // K)
        X = K
    else:
        D = ((N // K) + 1)
        X = (N % K)
        
    print(D, X)
    

