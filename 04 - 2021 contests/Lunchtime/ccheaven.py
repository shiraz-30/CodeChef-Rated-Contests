t = int(input())
for q in range(0, t):
    L = int(input())
    no_of_zeroes = 0
    no_of_ones = 0
    
    S = str(input())

    x = 0
    
    for i in range(0, len(S)):
        if S[i] == "0":
            no_of_zeroes += 1
        else:
            no_of_ones += 1
            
        if (no_of_ones >= no_of_zeroes):
            x = 1
            break 
        
    if x == 0:
        print("NO")
    else:
        print("YES")
            
    
