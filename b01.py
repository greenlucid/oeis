import itertools
import math
#get all non mirrored perms per range

p = []

for i in range(2,12):
  p.append(list(itertools.permutations(range(1,i+1))))
  #j=0
  #while j < len(p[i-2])-1: 
  #  if p[i-2][j][0] < p[i-2][j][-1]:
  #    p[i-2].pop(j)
  #    j-=1
  #  j+=1
t = [0,1]
l = [ [], [1] ]
for i in range(len(p)):
  max_distance = int( (i+2)**2 // 2 - 1 )
  max_list = []
  for j in range(len(p[i])):
    summ = 0
    s = p[i][j]
    #print("debug " +str(s))
    k = [0]*len(s)
    for ii in range(len(s)):
      k[int(s[ii])-1] = ii
    #print("tenemos " + str(k))
    for ii in range(len(s)-1):
      summ += abs(k[ii] - k[ii+1])
    
    if summ == max_distance:
      max_list.append(s)
  l.append(max_list)
  t.append(len(max_list))
print(t)
#print(l)
