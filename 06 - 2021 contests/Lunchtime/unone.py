t = int(input())
for q in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    li_1 = []
    li_2 = []
    
    for i in range(0, len(arr)):
        if (arr[i] % 2 == 0):
            li_1.append(arr[i])
        else:
            li_2.append(arr[i])
            
    
    while (len(li_1)):
        print(li_1[len(li_1) - 1], end = " ")
        li_1.pop()
        
    while (len(li_2)):
        print(li_2[len(li_2) - 1], end = " ")
        li_2.pop()
        
    print()
    