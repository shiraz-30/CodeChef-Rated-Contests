from collections import *

t = int(input())
for q in range(0, t):
	n = int(input())
	arr = list(map(int, input().split()))
	brr = list(map(int, input().split()))

	x = 10 ** 10

	arr.sort()
	brr.sort()

	temp = defaultdict(int)

	for i in range(0, n - 1):
		x = brr[i] - arr[i]
		y = brr[i] - arr[i + 1]

		if (x != y):
			if (x > 0):
				temp[x] += 1
			if (y > 0):
				temp[y] += 1
		else:
			if (x > 0):
				temp[x] += 1

	for j in temp.keys():
		if temp[j] == (n - 1):
			x = min(x, j)

	print(x)

