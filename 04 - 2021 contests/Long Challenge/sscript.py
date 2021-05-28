t = int(input())
for i in range(0, t):
    N, K = map(int, input().split())
    
    S = str(input())
    cnt = 0
    temp = 0
    for i in range(0, N):
        
        if (S[i] == '*'):
            cnt += 1
            if (cnt >= temp):
                temp = cnt
        else:
            cnt = 0
            
    if (temp >= K):
        print("Yes")
    else:
        print("No")
        