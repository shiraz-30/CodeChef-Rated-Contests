t = int(input())
for i in range(0, t):
    n, a, b = map(int, input().split())
    sarthak = 0
    anuradha = 0
    
    for j in range(0, n):
        S = input()
                            
        if (S[0] == "E" or S[0] == "Q" or S[0] == "U" or S[0] == "I" or S[0] == "N" or S[0] == "O" or S[0] == "X"):
            sarthak += a
                
        else:
            anuradha += b
                
    if (sarthak > anuradha):
        print("SARTHAK")
    elif (anuradha > sarthak):
        print("ANURADHA")
                
    else:
        print("DRAW")
                
