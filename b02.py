import math

def divsum(n):
	"""Returns the sum of all numbers that divide n, except itself."""
	sum = -n
	limit = int(math.sqrt(n))+1
	for i in range( 1, limit ):
		if n%i == 0 :
			if n//i == i:
				sum += i
			else:
				sum += i + n//i
	return sum


for i in range(4,20):
	print(i, " ",divsum(i))