#Tomas 'Green' Roca Sanchez
#Sum of distance sums of all permutations of n elements
#The name of this series is C01 locally.
#Found to be A090672 in oeis

import itertools

def sum_of_distances(n):
    p = list(itertools.permutations(range(1,n+1)))
    summ = 0
    for j in p:
        summ += distance_sum(j)
    return summ


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

l = []
for i in range(1,8):
    l.append(sum_of_distances(i))
print(l)