#Prime Number Check and generator

import math, random

def isPrimeTrialDiv(num):
    # Returns True if num is a prime number, otherwise False
    #Uses the trial division algorithem for testing primality.
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primeSieve(sieveSize):
    #Returns a list of prime numbers calculated using the Sieve of Eratosthenes
    #algorithm

    sieve = [True] * sieveSize
    sieve[0] = False # Zero and one are not prime numbers
    sieve[1] = False

    #Create the sieve:
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
    #Compiles the list of primes:
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)
    return primes

def rabinMiller(num):
    #Returns True if num is a prime number.
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        #Keep halving s until it is odd (and use t to count how many times we halve s)
        s = s // 2
        t += 1
    for trials in range(5): #Try to falsify num's primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # This test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

#Most of the time we can determine if a num is not prime quickly by dividing the first
#few dozen prime numbers. This is quicker than rabinMiller() but does not detect all
#composites

LOW_PRIMES = primeSieve(100)

def isPrime(num):
    #Return true if num is prime. Function does a quicker prime number check before
    #calling rabinMiller()
    if (num < 2):
        return False
    for prime in LOW_PRIMES:
        if (num % prime == 0 and prime != num):
            return False

    return rabinMiller(num)

def generateLargePrime(keysize=1024):
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num


def main():
    p = primeSieve(101)
    q = isPrime(100)
    largePrime = generateLargePrime()
    print(p)
    print(q)
    print(largePrime)
    pass

if __name__ == '__main__':
    main()
