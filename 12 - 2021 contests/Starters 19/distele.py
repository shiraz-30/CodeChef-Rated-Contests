t = int(input())
for q in range(0, t):
	n = int(input())
	li = list(map(int, input().split()))

	mod = 10**9 + 7

	freq = {}
	res = 1 
	arr = []

	for i in li:
		if (i in freq):
			freq[i] += 1 
		else:
			freq[i] = 1 

	for key, value in freq.items():
		arr.append(value)

	x = len(arr)

	for j in range(0, x):
		res *= arr[j] + 1
		res %= mod

	res -= 1

	print(res)
