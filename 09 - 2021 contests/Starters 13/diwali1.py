t = int(input())
for q in range(0, t):
	p, a, b, c, x, y = map(int, input().split())

	res1 = (b + (a * x))
	res2 = (c + (a * y))

	temp = min(res1, res2)
	ans = (p // temp)

	print(ans)
