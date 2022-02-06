def is_power(n):
	if (n != 0 and (n & (n - 1)) == 0):
		return True
	else:
		return False

t = int(input())
for q in range(0, t):
	n = int(input())


	if (n == 2):
		print("Bob")
	if (n == 1):
		print("Alice")

	if (n % 2 == 0 and n >= 3):
		if (is_power(n + 2) == True):
			print("Bob")
		else:
			print("Alice")

	if (n % 2 != 0 and n >= 3):
		if (is_power(n + 1) == True):
			print("Alice")
		else:
			print("Bob")

