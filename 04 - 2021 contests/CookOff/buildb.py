t = int(input())
for i in range(0, t):
    N, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    tension = 0
    max_value = 0
    y = 0
    
    for j in range(0, N):
        tension += B[j]
        
        if max_value < tension:
            max_value = tension
            
        if j < N - 1:
            y = (R * (A[j + 1] - A[j]))
            
        if y <= tension:
            tension -= y
        else:
            tension = 0 
        
    print(max_value)

