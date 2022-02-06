def no_of_divisibles(l, r):
	if (l % 3 == 0):
		return ((r // 3) - (l // 3)) + 1

	return ((r // 3) - (l // 3))

t = int(input())
for i in range(0, t):
	l, r = map(int, input().split())

	print(no_of_divisibles(l, r))
