#Tomas 'Green' Roca Sanchez
#This returns numbers with v values for sum of proper divisors of n
#This is a second attempt, using a more complicated method, that should be more efficient nonetheless

#The algorithm is inputted nmax and v, and will return all smaller numbers that met the condition

#Get all primes up to nmax**2. This should be done faster with a prime sieve. O(n**2)
def prime_sieve(n):
    sieve = range(n+1)
    c = 2
    while 
#Create a listFactor of empty lists and weave a p in every p steps, then another every p**2, for every prime
#for every listFactor entry, create a temporal buffer to append unique divisors
#get all different divisors, add them up, and store the result in divsumList