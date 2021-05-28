t = int(input())
for i in range(0, t):
    

    k1, k2, k3, v = map(float, input().split())
    x = (k1*k2*k3*v)
    a = (100 / x)
    y = round(a, 2)

    if (y < 9.58):
        print("Yes")
    else:
        print("No")
    