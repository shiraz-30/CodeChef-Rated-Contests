t = int(input())
for q in range(0, t):
	n = int(input())

	ans = []

	if (n % 2):
		print("YES")

		for i in range(1, n//2 + 1):
			ans.append(i)
		ans.append(n)

		for j in range(n - 1, n//2, -1):
			ans.append(j)

		print(*ans)

	elif (n != 2):
		print("YES")

		ans.append(n//2)
		for i in range(1, n//2):
			ans.append(i)
		for j in range(n, n//2, -1):
			ans.append(j)

		print(*ans)

	else:
		print("NO")

