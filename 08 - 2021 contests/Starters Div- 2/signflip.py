t = int(input())
for q in range(0, t):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))

	arr.sort()

	for i in range(0, k):
		if (arr[i] < 0):
			arr[i] *= -1

	sum_arr = 0

	for j in range(0, n):
		if (arr[j] > 0):
			sum_arr += arr[j]

	print(sum_arr)
