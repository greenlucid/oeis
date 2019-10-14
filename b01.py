import itertools
import math

p = []
#generate permutations in p
for i in range(2,10):
  p.append(list(itertools.permutations(range(1,i+1))))
l = [ [], [1] ]
for i in range(len(p)):
  #this is the maximum distance as explained in A047838
  max_distance = int( (i+2)**2 // 2 - 1 )
  #this will store all different permutations that arrive to this max
  max_list = []
  for j in range(len(p[i])):
    summ = 0
    s = p[i][j]
    k = [0]*len(s)
    for ii in range(len(s)):
      k[int(s[ii])-1] = ii
    for ii in range(len(s)-1):
      summ += abs(k[ii] - k[ii+1])
    if summ == max_distance:
      max_list.append(s)
  l.append(max_list)
  t.append(len(max_list))
print(t)
