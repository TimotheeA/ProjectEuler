def puiss(x,n) :
	X = 1
	for i in range(0, n) :
		X = X*x
	return(X)

x = puiss(2,1000)
x = str(x)
t = 0

for i in range(0, len(x)) :
	t = t+int(x[i])

print (t)