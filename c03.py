#Tomas 'Green' Roca Sanchez
# n has the same number of prime factors than n+1
# found to be A045920

import math

primeListLen = 10000
pl = [2,3]
def isPrime(a):
  if(a == 1 or a%2==0 or a%3==0):
    return False
  else:
    k=1
    while k*6-1<=math.sqrt(a):
      if(a%(k*6-1)==0 or a%(k*6+1)==0):
        return False
      k+=1
    return True
pl = [2,3]
i = 5
while len(pl) < primeListLen :
  if isPrime(i):
    pl.append(i)
  i+=2
def deco(a):
  i = 0
  fac = []
  c = a
  sqrt = int(math.sqrt(c))
  while pl[i] <= sqrt:
    while pl[i] <= sqrt and c%pl[i]==0:
      fac.append(pl[i])
      c//=pl[i]
    i+=1
  if c!=1:
    fac.append(c)
  return fac


deco_list = [[],[]]
for i in range(2,10000):
    deco_list.append(deco(i))

sol_list = []
for i in range(len(deco_list)-1):
    if len(deco_list[i]) == len(deco_list[i+1]):
        sol_list.append(i)
print(sol_list)