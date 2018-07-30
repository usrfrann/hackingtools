# Affine Cipher

import sys, pyperclip, cryptoMath, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
    myMessage = """"A computer would deserve to be called intelligent if it could
    deceive a human into believing that it was human."
    -Alan Turing"""
    myKey = getRandomKey()   # 2894
    myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (myMode))

#Shannon's Maxim
def getKeyParts(key):
    keyA = key // len(SYMBOLS) # 2894 // 66 = 43
    keyB = key % len(SYMBOLS)  # 2894 % 66 = 56
    # 43 * 66 + 56 = 2894 One key broken down into two numbers
    return (keyA,keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Affine Cipher is weak when key A is set to 1. Use a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Affine cipher is weak when key B is set to 0. Use a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if cryptoMath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit("""Key A (%s) and the symbol set size (%s) are not relatively
         prime. Choose a different key.""" % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA,keyB,'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            #Encrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol #Append the symbol without encryoting.
    return ciphertext

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptoMath.findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            #Decrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext = SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # Append the symbol without decrypting
    return plaintext

#Oppsite of get keyParts
def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptoMath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB




if __name__ == '__main__':
   main()


