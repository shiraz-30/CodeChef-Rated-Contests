t = int(input())
for q in range(0, t):
	n = int(input())
	s = input()

	check = True
	x, y = 0, 0

	for i in range(0, len(s)):
		if (s[i] == "0"):
			x += 1
		else:
			y += 1

	temp = min(x, y)

	if (temp == 0):
		check = False
	if (temp == 1):
		check = True
	if (temp >= 2):
		ans = (x + y - (2 * temp))
		if (ans % 2 == 0):
			check = False

	if (check == True):
		print("Alice")
	else:
		print("Bob")
