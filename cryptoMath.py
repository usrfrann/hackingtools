#Cryptomath Module

#Euclid algorithm
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#Modular inverse (a * i) % m == 1

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None # No mod inverse if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator.
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3),v1,v2,v3
    return u1 % m

def main():
    print("The Greatest Common Denomenator of 32 and 24: " + str(gcd(24,32)))
    print("Mod Inverse 7 26: " + str(findModInverse(7,26)))

if __name__ == '__main__':
    main()



