t = int(input())
for q in range(0, t):
	a, b = map(int, input().split())

	temp = 60

	while (b % a != 0 and temp):
		if (b > a):
			b %= a 
		elif (b < a):
			b *= b
		elif (b == 1):
			b = 1

		temp -= 1

	if (b % a == 0):
		print("YES")
	else:
		print("NO")

