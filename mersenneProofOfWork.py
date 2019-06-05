import math
import time

def mersenneWork(n, prime):
    # Initialize all entries of boolean
    # array as true. A value in prime[i]
    # will finally be false if i is Not
    # a prime, else true bool prime[n+1]
    for i in range(0, n + 1):
        prime[i] = True

    p = 2
    while (p * p <= n):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False

        p += 1

# Function to generate mersenne
# primes less than or equal to n
def mersennePrimes(n):
    # Create a boolean array
    # "prime[0..n]"
    prime = [0] * (n + 1)

    # Generating primes using Sieve
    mersenneWork(n, prime)

    # Generate all numbers of the
    # form 2^k - 1 and smaller
    # than or equal to n.
    k = 2
    while (((1 << k) - 1) <= n):

        num = (1 << k) - 1

        # Checking whether number
        # is prime and is one
        # less then the power of 2
        if (prime[num]):
            #print(num)
            largePrime = num

        k += 1
    return largePrime,math.log(largePrime+1,2)

n = 150000000
#print("Mersenne prime numbers smaller",
              #"than or equal to " , n )
#num,p = mersennePrimes(n) # 524287 (2^28-1)
#print(num,p)

def isPrime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, num // 2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True

    else:
        return False

def verify(n,num):
    print(num)
    print(2**n-1)
    if(2**n-1 != num):
        return False
    return isPrime(num)


timeStart = time.time()
x = verify(19,(2**19-1))
timeEnd = time.time()
print(x)
print(timeEnd-timeStart)
