#Tomas 'Green' Roca Sanchez
#There is no number whose divisor sum except themselves is equal to the numbers in this series.

import math

#the biggest number for which we will search for indexed numbers
nMax = 1000

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

def divsumList(n):
    """Returns a list with all divsums of numbers 0 to n."""
    #initialize list with preset values
    sumlist = [0, 0]
    for i in range(2, n+1):
        sumlist.append(divsum(i))
    return sumlist

def indexedList(sumlist):
    """Given a divsumList, it creates a new list, appending, for each position, all numbers with divsum equal to that division."""
    #0 and 1 have divsum 0, so they are in zero position
    indexed = [[] for i in range(nMax+1)]
    indexed[0].append(0)
    indexed[0].append(1)

    for i in range(2,len(sumlist)):
        if sumlist[i] <= nMax:
          indexed[sumlist[i]].append(i)

    return indexed


greatList = indexedList(divsumList(nMax**2))
specialList = []
for i in range(len(greatList)):
    #print (i,": ",greatList[i])
    if len(greatList[i])==0:
        specialList.append(i)

print(specialList)