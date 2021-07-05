#Unrated Problem

t = int(input())
for i in range(0, t):
    A, B, X = map(int, input().split())
    
    p = (B - A)
    q = (p // X)  
    
    print(q)
    