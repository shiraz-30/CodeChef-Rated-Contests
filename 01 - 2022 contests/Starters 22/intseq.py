t = int(input())
for q in range(0, t):
	k = int(input())

	if (k / 2 == 1):
		print(1)
	else:
		temp = 0

		while(k % 2 == 0):
			temp += 1
			k //= 2
		print(temp)
