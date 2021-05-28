t = int(input())
for i in range(0, t):

    n, m = map(int,input().split())
    x, y = map(int,input().split())
    a, b = map(int,input().split())

    thief = (m - y + n - x)
    
    if ((m - b) > (n - a)):
        police = (m - b)
    else:
        police = (n - a)

    if (police < thief):
        print("NO")
    else:
        print("YES")
