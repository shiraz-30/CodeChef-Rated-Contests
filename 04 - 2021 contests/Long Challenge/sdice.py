t = int(input())
for i in range(0, t):
    n = int(input())
    x = (n % 4)
    y = ((n - x) // 4)
    if (n == 1):
        print(6 + 5 + 4 + 3 + 2)
    elif (n == 2):
        print(2*(6 + 5 + 4 + 3))
    elif (n == 3):
        print(2*(6 + 5 + 4 + 3) + (6 + 5 + 4))
    elif (n == 4):
        print(4*(6 + 5 + 4))
    else:
        ans = (y*(4*(6 + 5)))
        
        if x == 0:
            ans += (4 * 4)
        elif x == 1:
            ans += ((3 * 4) + (6 + 5 + 4 + 3 + 2))
        elif x == 2:
            ans += ((2 * 4) + (2 *(6 + 5 + 4 + 3)))
        elif x == 3:
            ans += ((1 * 4) + (2 *(6 + 5 + 4 + 3)) + (6 + 5 + 4))
            
        print(ans)
        
        