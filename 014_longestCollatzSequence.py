def collatz(i) :
	t = []
	while i > 1 :
		t.append(i)
		if i/2 == int(i/2) :
			i = i/2
		else :
			i = 3*i+1
	return  len(t) 	

a=0
x=0
i=13
while i < 1000000 :
	i = i+1
	print(i)
	if x < collatz(i) :
		x = collatz(i)
		a = i

print(a)
print(x)
