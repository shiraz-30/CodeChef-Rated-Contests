t = int(input())
for q in range(0, t):
	n = int(input())

	li = []
	li.append(n)

	for i in range(1, n):
		li.append(i)

	print(*li)
