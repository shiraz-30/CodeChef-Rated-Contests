t = int(input())
for i in range(0, t):
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    ans = [0]*N
    
    for j in range(0, N):
        result = str(input())
        arr = list(result)
        
        no_of_F = arr.count('F')
        no_of_P = arr.count('P')

        if (no_of_F >= X) or (no_of_F == X - 1 and no_of_P >= Y):
            ans.append('1')

        else:
            ans.append('0')

        print(ans[-1], end = "")
        
    print("")

