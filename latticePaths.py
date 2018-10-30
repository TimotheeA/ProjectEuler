from funcGrid import *

def tabBin(n, l) :
	t = createMTabNZero(1, l)
	i = 0
	while n >= 1 :
		i = i+1
		t[0][l-i] = n%2
		n = int(n/2)
	return t


def puiss(x,n) :
	X = 1
	for i in range(0, n) :
		X = X*x
	return(X)

def sommeTab(t) :
	x = 0
	for i in range(0, len(t[0])) :
		x = x + t[0][i]
	return x

grid = 20
t = createMTabNZero(1,grid+1)

for i in range(0, puiss(2, grid)) :
	x = tabBin(i, grid)
	c1 = 0
	for j in range (0,grid) :
		if x[0][j] == 1 :
			c1 = c1 + 1
	t[0][c1] = t[0][c1] + 1

c = 0
for i in range(0, int(grid)+1) :
	c = c + t[0][i] * t[0][grid-i] 
	print(t[0][i], t[0][grid-i])

print(t)
print(c)