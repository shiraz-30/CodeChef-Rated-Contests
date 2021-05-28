A, B, C = list(map(int, input().split()))
arr = [A, B, C]
x = set(arr)
if (len(arr) == len(x)):
    print("No")
else:
    print("Yes")
    