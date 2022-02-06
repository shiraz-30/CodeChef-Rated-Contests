t = int(input())
for q in range(0, t):
	n = int(input())


	arr = []
	res = []

	for a in range(0, 17):
		for b in range(a + 1, 18):
			for c in range(b + 1, 19):
				for d in range(c + 1, 20):
					ans = ((1 << a) + (1<<b) + (1<<c) + (1<<d))

					arr.append(ans)

				if (len(arr) == 1000):
					break
			if (len(arr) == 1000):
				break
		if (len(arr) == 1000):
			break

	for i in range(0, n):
		res.append(arr[i])

	print(*res)

	
