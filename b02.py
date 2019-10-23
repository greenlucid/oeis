import math

def divsum(n):
	"""Returns the sum of all numbers that divide n, except itself."""
	sum=-n
	for i in range( 1, int(math.sqrt(n)) ):
		if n%i==0:
			sum+=i + n/i
	if n%int(math.sqrt(n))==0:
		sum+=int(math.sqrt(n))
	return sum


for i in range(1,20):
	print(i, " ",divsum(i))