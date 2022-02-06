t = int(input())
for q in range(0, t):
	a, b, p, q = map(int, input().split())

	if (a == p and b == q):
		print(0)
	else:
		if (((a + b) % 2 == 0 and (p + q) % 2 == 0) or ((a + b) % 2 != 0 and (p + q) % 2 != 0)):
			print(2)
		else:
			print(1)
