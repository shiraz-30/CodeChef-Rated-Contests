t = int(input())
for q in range(0, t):
	s = input()

	if (s[0] == "0"):
		count = 1
	else:
		count = 0

	for i in range(0, len(s) - 1):
		if (s[i] != s[i + 1]):
			count += 1

	print(count)
