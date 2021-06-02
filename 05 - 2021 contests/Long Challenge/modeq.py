t = int(input())
for q in range(0, t):
    N, M = map(int, input().split())
    count = 0
    result = [1] * (N + 1)
    
    for i in range(2, N + 1):
        rem = (M % i)
        count += result[rem]
        
        for j in range(rem, N + 1, i):
            result[j] += 1
            
    print(count)
     