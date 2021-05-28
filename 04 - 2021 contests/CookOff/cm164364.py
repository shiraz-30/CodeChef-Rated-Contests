def maxoccur(arr,x ):
    
    lena = len(arr)
    lens = len(set(arr))
    excess = lena - lens
    return lens if excess >= x else max(0, lena - x)





t = int(input())
for i in range(0, t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    print(maxoccur(arr, x))    
