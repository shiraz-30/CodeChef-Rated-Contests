t = int(input())
for q in range(0,t):
	n, p, x, y = map(int, input().split())
	arr = list(map(int, input().split()))

	z = p
	li = arr[:z]
	no_of_0 = li.count(0)
	no_of_1 = li.count(1)

	a = (no_of_0 * x)
	b = (no_of_1 * y)

	print(a + b)

