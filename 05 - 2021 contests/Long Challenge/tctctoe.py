t = int(input())
for i in range(0, t):
    
    count_of_X = 0
    count_of_O = 0
    count_of_underscore = 0
    li = []
    
    for q in range(0, 3):
        ele = input()
        li.append(ele)
        
    for j in range(0, 3):
        for k in range(0, 3):
            
            if li[j][k] == "X":
                count_of_X += 1
                
            elif li[j][k] == "O":
                count_of_O += 1
                
            elif li[j][k] == "_":
                count_of_underscore += 1
                
    winner_is_X = 0
    winner_is_O = 0
    
    
    if li[0][0] == "X" and li[0][1] == "X" and li[0][2] == "X":
        winner_is_X = 1
    
    if li[1][0] == "X" and li[1][1] == "X" and li[1][2] == "X":
        winner_is_X = 1
    
    if li[2][0] == "X" and li[2][1] == "X" and li[2][2] == "X":
        winner_is_X = 1
        
    if li[0][0] == "X" and li[1][0] == "X" and li[2][0] == "X":
        winner_is_X = 1
        
    if li[0][1] == "X" and li[1][1] == "X" and li[2][1] == "X":
        winner_is_X = 1
        
    if li[0][2] == "X" and li[1][2] == "X" and li[2][2] == "X":
        winner_is_X = 1
        
    if li[0][0] == "X" and li[1][1] == "X" and li[2][2] == "X":
        winner_is_X = 1
        
    if li[0][2] == "X" and li[1][1] == "X" and li[2][0] == "X":
        winner_is_X = 1 
        
    if li[0][0] == "O" and li[0][1] == "O" and li[0][2] == "O":
        winner_is_O = 1
    
    if li[1][0] == "O" and li[1][1] == "O" and li[1][2] == "O":
        winner_is_O = 1
    
    if li[2][0] == "O" and li[2][1] == "O" and li[2][2] == "O":
        winner_is_O = 1
        
    if li[0][0] == "O" and li[1][0] == "O" and li[2][0] == "O":
        winner_is_O = 1
        
    if li[0][1] == "O" and li[1][1] == "O" and li[2][1] == "O":
        winner_is_O = 1 
        
    if li[0][2] == "O" and li[1][2] == "O" and li[2][2] == "O":
        winner_is_O = 1
        
    if li[0][0] == "O" and li[1][1] == "O" and li[2][2] == "O":
        winner_is_O = 1
        
    if li[0][2] == "O" and li[1][1] == "O" and li[2][0] == "O":
        winner_is_O = 1 
        
    
    if (winner_is_X == 1 and winner_is_O == 1) or (count_of_X - count_of_O < 0) or (count_of_X - count_of_O > 1):
        print(3)
        
    elif (count_of_X == 0) and (count_of_O == 0) and (count_of_underscore == 9):
        print(2)
        
    elif (winner_is_X == 1) and (winner_is_O == 0) and (count_of_X > count_of_O):
        print(1)
        
    elif (winner_is_X == 0) and (winner_is_O == 1) and (count_of_X == count_of_O):
        print(1)
        
    elif (winner_is_X == 0) and (winner_is_O == 0) and (count_of_underscore == 0):
        print(1)
        
    elif (winner_is_X == 0) and (winner_is_O == 0) and (count_of_underscore > 0):
        print(2)
        
    else:
        print(3)
        

