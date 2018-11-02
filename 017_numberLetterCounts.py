digit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ,"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "and", "thousand"]

def lettre(t) :
	t = str(t)
	n = ["0","0","0"]
	for i in range(0, len(t)) :
		n[len(n)-i-1] = t[len(t)-i-1]
		print(n)

	if (int(n[1]) > 1) :
		nl = digit[int("2"+n[1])] + digit[int(n[2])]
	else :
		nl = digit[int(n[1]+n[2])]
		
	if ((int(n[0]) >= 1) and (len(nl) > 0)) :
		nl = digit[int(n[0])] + digit[30] + digit[31] + nl
	elif (int(n[0]) >= 1) :
		nl = digit[int(n[0])] + digit[30] + nl

		#rien
	return nl

s = 11
for i in range(1, 1000) :
	s = s + len(lettre(i))

print(s)

