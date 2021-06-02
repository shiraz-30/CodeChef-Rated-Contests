t = int(input())
for p in range(0, t):

    n, k = map(int, input().split())
    s = input()

    initialCount = 0

    for i in range(1, n):

        if (s[i - 1] == s[i]):
            initialCount += 2
        else:
            initialCount += 1

    x = list(s)
    li = map(int, input().split())

    if(n == 1):
        print(0)
    else:
        for q in li:
                        
            if x[q - 1] == "1":
                x[q - 1] = "0"
            else:
                x[q - 1] = "1"
                
            if (q == n):

                if x[q - 1] == x[q - 2]:
                    initialCount += 1
                else:
                    initialCount -= 1
                    
            elif (q == 1):

                if x[0] == x[1]:
                    initialCount += 1
                else:
                    initialCount -= 1

            else:

                if x[q - 1] == x[q - 2]:
                    initialCount += 1
                else:
                    initialCount -= 1
                    
                if x[q - 1] == x[q]:
                    initialCount += 1
                else:
                    initialCount -= 1
                    
            print(initialCount)
        