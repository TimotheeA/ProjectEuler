from math import *

def diviseurN(n) :
	t = []
	for i in range (1, int(sqrt(n+1))) :
		if n/i == int(n/i) :
			t.append(i)
	return t

	return t
def triangleN(n) :
	x = 0
	for i in range(1, n+1) :
		x = x+i
	return x

t = []
i = 0
while len(t) <= 250 :
	i=i+1
	x = triangleN(i)
	t = diviseurN(x)
	print(i, len(t))

print(i)
print(x)

