# Tomas 'Green' Roca Sanchez
# b02.1 : F(n) has same number of prime factors than F(n+1), with F(a) being the Fibonacci sequence
# b02.2 : The specific Fibonacci numbers
# b02.3 : Number of prime factors of F(n)
# Instead of having to factor these numbers, I fetched a file with the first 1000 Fibonacci factorizations
# Credit to http://mersennus.net/fibonacci/ marin.mersennus@gmail.com
# So this script only has to load in the information and compare it with itself


f = open("f1000.txt", "r")
data = f.readlines()
#Stores the list of factors for each element. F(0), F(1) and F(2) are non applicable
fibf = [[],[],[]]

#process and store the input data
for i in range(3,1001):
    cur = []
    j = 0
    
    while data[i][j]!='=':
        j+=1
    j+=1
    lastj = j
    while j < len(data[i]):
        if data[i][j] == '*':
            cur.append(data[i][lastj+1:j-1])
            lastj=j+1
        j+=1
    cur.append(data[i][lastj+1:j-1])

    fact = []
    for st in cur:
        if '^' in st:
            # search for ^ as breakpoint
            j = len(st)-2
            while st[j] != '^':
                j-=1
            a = int(st[:j])
            b = int(st[j+1:])
            for ii in range(b):
                fact.append(a)
        else:
            fact.append(int(st))
    fibf.append(fact)

s_1 = [0,1]
s_2 = [0,1]
s_3 = [0,0,0]
for i in range(3,len(fibf)-1):
    if len(fibf[i]) == len(fibf[i+1]):
        s_1.append(i)
        mul = 1
        for j in fibf[i]:
            mul*=j
        s_2.append(mul)
    s_3.append(len(fibf[i]))
print("s_1: ", s_1)
print("s_2: ", s_2)
print("s_3: ", s_3)