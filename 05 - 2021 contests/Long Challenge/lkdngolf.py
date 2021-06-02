t = int(input())
for i in range(0, t):
    N, x, k = map(int, input().split())
    
    if (x % k == 0) | ((N + 1 - x) % k == 0):
        print("YES")
    else:
        print("NO")
        

    