t = int(input())
for q in range(0, t):
    s = str(input())
    
    x = s[0]
    y = int(x)
    z = s[1:]
    p = "1" + s
    q = x + "0" + z
    
    if (y - 1 > 0):
        print(p)
    else:
        print(q)
        