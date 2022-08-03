from numpy import random
import math

n = 4
weight = [13, 14, 15, 10, 12, 20 ] #n choose 2.


save = [0 for i in range(n)]
maxval = -1
for i in range(10**6):
	x=random.random(size=(n))
	first = 0
	index = 0
	for i in range(n):
		for j in range(i+1,n):
			first += weight[index] * x[i]*x[j]
			index +=1

	second = sum([c**2 for c in x])
	# second = (x[0]+x[1]+x[2])**2
	r = first/second
	
	if(r>maxval):
		maxval = r
		save = x

print(maxval)
print(x)
print(save)

print(math.sqrt(sum([x**2 for x in weight])) * math.sqrt((n-1)/(2*n)))
