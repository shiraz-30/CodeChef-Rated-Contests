t = int(input())
for i in range(0, t):
    N, M = map(int, input().split())
    
    mod = (10 ** 9 + 7)
    x = (pow(2, N, mod) - 1)
    y = pow(x, M, mod)
    
    print(y)
    
   