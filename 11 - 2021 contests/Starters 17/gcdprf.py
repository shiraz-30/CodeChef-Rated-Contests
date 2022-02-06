t = int(input())
for q in range(0, t):
	n = int(input())
	li = list(map(int, input().split()))
	
	x = 0
	for j in range(1, n):
		if (li[j - 1] % li[j] != 0):
			x = 1

	if (x == 0):
		for i in range(0, n):
			print(li[i], end = " ")
		print()
	if (x == 1):
		print(-1)
