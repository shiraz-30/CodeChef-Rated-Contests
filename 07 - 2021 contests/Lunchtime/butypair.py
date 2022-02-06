t = int(input())
for q in range(0, t):
	n = int(input())
	arr = list(map(int, input().split()))

	freq = {}
	x = 0

	for item in arr:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	y = freq.values()
	z = list(y)
	
	
	for i in range(0, len(z)):
		if z[i] == 1:
			x += (n - 1)
		elif z[i] != 1:
			p = z[i] % (10 ** 7)
			x += (n - z[i]) * p 

	print(x)
