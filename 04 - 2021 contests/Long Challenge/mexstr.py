# Partially Correct [20 pts]

t = int(input())
for p in range(0, t):
    S = input()
    
    if "0" not in S:
        print(0)
    else:
        for q in range(0, 65):
            binary_no = bin(int(q)).replace("0b", "")
            digits_rem = len(binary_no)
            result = 0
            last_index = -1
            
            for i in range(0, len(binary_no)):
                decimal_no_to_be_taken = binary_no[i]
                
                for j in range(last_index + 1, len(S)):
                    if S[j] == decimal_no_to_be_taken:
                        digits_rem -= 1
                        last_index = j
                        break
                         
            if (digits_rem != 0):
                result = q
                break
            
        result = bin(int(q)).replace("0b", "")
        
        print(result)

        
        