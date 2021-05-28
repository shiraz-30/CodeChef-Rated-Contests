n = int(input())
a = sum(list(map(int,input().split())))
q = int(input())
x = sum(list(map(int,input().split())))

mod = int(1e9 +7)

for i in range(1, q + 1):
    a = (a * 2)

    print(a % mod)
    