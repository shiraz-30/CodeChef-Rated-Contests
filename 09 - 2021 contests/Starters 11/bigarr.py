t = int(input())
for i in range(0, t):
	n, s = map(int, input().split())

	ans = sum(range(1, n + 1))
	x = (ans - s)

	if (x > 0 and x <= n):
		print(x)
	else:
		print(-1)
