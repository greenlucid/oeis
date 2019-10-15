#Tomás 'Green' Roca Sánchez
#Number of different permutations of length n that possess maximum orderedly contigual distance sum
#The name of this series is B01 locally and will possess a different name in OEIS
import itertools

def max_distance(n):
	'''Returns the maximum possible distance a permutation of length n, as explained in A047838'''
	return n**2 // 2 - 1

def distance_sum(s):
	'''Returns the sum of all orderedly contigual distances of the permutation'''
	summ = 0
	k = [0]*len(s)
	#stores the position of every integer
	for ii in range(len(s)):
		k[int(s[ii])-1] = ii
	#adds up the offset
	for ii in range(len(s)-1):
		summ += abs(k[ii] - k[ii+1])
	return summ

def different_maximums(n):
	'''Returns how many different permutations of length n possess maximum distance sum'''
	p = list(itertools.permutations(range(1,n+1)))
	count = 0
	#store max_distance to avoid recalculating too many times
	maxx = max_distance(n)
	for i in p:
		if maxx == distance_sum(i): count+=1
	return count
#A047838 formula is innacurate for the first two elements:
#There is 1 way to obtain maximum distance sum for all permutations of zero elements: []
#And there is also 1 way to do the same for all permutations of one element: [1], and thus:
b01 = [1, 1]
for i in range(2, 8):
	b01.append(different_maximums(i))
print(b01)