#Unrated Problem

t =int(input())
for q in range(0, t):
       n,k = list(map(int , input().split()))
       arr = list(map(int , input().split()))

       ans = 0
       arr.sort(reverse = True)
       
       for i in range(0, 2 * k - 1, 2):
              ans += arr[i]
       
       res=0

       for j in range(1, 2 * k, 2):
              res += arr[j]
       
       res += arr[2 * k]
       
       print(max(res , ans))

