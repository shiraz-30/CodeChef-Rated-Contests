def XOR_equality(expo):
    mod = 10**9 + 7
    
    if (expo == 0):
        return (1 % mod)
    elif (expo == 1):
        return (2 % mod)
        
    power = XOR_equality(expo // 2)
        
    if (expo & 1):
        return (2 * power * power) % mod
    else:
        return (power * power) % mod 
    

t = int(input())
for i in range(0, t):
    N = int(input())
    expo = N - 1
    
    print(XOR_equality(N - 1))
    

    
    
    
    
