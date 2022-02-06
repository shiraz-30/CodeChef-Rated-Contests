t = int(input())
for q in range(0, t):

	n, k = map(int, input().split())
	arr = list(map(int, input().split()))

	x = max(arr)
	y = arr.index(x)

	s = set()
	for i in range(0, n):
		if (arr[i] == x):
			s.add(i)
	
	cnt = 0

	for j in s:
		z = (j - k + 1)

		if (z >= 0):
			cnt += (n - j)

	print(cnt)

