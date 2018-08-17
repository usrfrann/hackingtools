#Public Key Generator

import random, sys, os, primeNum, cryptomath

def main():
    print('Making key files...')
    makeKeyFiles('key', 1024)
    print('Key files made.')
    pass

def generateKey(keySize):
    p = 0
    q = 0
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p * q

    print('Generating e that is realativly prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)

    print('Public key', publicKey)
    print('Private key', privateKey)

    return publicKey, privateKey

def makeKeyFiles(name, keySize):
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
            sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exist' % (name,name))
    publicKey, privateKey = generateKey(keySize)
    print()
    print('The public key is a %s and %s digig number.'
        % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0],publicKey[1]))
    fo.close()

    print()
    print('The private key is a %s and a %s digit number.'
        % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, privateKey[0],privateKey[1]))
    fo.close()

if __name__ == '__main__':
    main()
