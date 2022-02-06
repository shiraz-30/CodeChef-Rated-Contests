t = int(input())
for q in range(0, t):
	n = int(input())
	arr = list(map(int, input().split()))

	odd, even = 0, 0

	for i in range(0, n):
		if (arr[i] % 2 == 0):
			even += 1
		else:
			odd += 1

	evenplaces, oddplaces = 0, 0

	if (n % 2 == 0):
		evenplaces, oddplaces = n // 2, n // 2
	else:
		evenplaces, oddplaces = (n // 2) + 1, n // 2

	if (even == evenplaces):
		print(n)
	elif (even > evenplaces):
		print(evenplaces + odd)
	else:
		print(even + oddplaces)

