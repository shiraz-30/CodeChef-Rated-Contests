def symmetric_pairs(weights, n):
    weights.sort()
    
    i = 0
    li = []
    while i < n - 1:
        if weights[i] == weights[i + 1]:
            li.append(weights[i])
            li.append(weights[i + 1])
            
            i = i + 2
        else:
            i += 1
            
    return sum(li) 
            
t = int(input())
for i in range(0, t):
    N, W, Wr = map(int, input().split())
    weights = list(map(int, input().split()))
    n = len(weights)
    
    check = symmetric_pairs(weights, n)
    x = Wr + check
    
    if x >= W:
        print("YES")
    else:
        print("NO")
        

    
    
    
