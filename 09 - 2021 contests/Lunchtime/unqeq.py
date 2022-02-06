t = int(input())
flag = True
for q in range(0, t):
	n = int(input())

	if (n % 4 != 0):
		print("NO")	
		flag = False	
	else:
		print("YES")
		flag = True

	a, b = 1, n 
	li1 = []
	li2 = []
	check1, check2 = 0, n // 2

	while(check2):

		if (check1 == 0):
			li1.append(a)
			a += 1
			check1 = 1
		else:
			li1.append(b)
			b -= 1
			check1 = 0

		check2 -= 1

	for i in range(a, b + 1):
		li2.append(i)

	li1.sort()
	li2.sort()

	if (flag == True):		
		print(*li1)
		print(*li2)
