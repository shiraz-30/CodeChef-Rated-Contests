t = int(input())
for q in range(0, t):
	n = int(input())

	if (n % 2 == 0):
		arr = [-1] * n 
		for i in range(0, n):
			print(*arr)
	else:
		for i in range(0, n):
			for j in range(0, n):
				if (i == j):
					print(-1, end = " ")
				else:
					print(1, end = " ")
			print()
