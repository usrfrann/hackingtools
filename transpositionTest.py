#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Living_computer
#
# Created:     24/07/2018
# Copyright:   (c) Living_computer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random,transpositionEncrypt,transpositionDecryption

def main():
    #random seed make sure that the random list uses the same set of random numbers
    #Static list of random values to test against instead of using the sys.time as
    #seed value
    random.seed(42)

    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)
        #message = 'Common Sense is not so Common'
        #convert message into list and shuffle it
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) #Converts back into string

        print('Test #%s: "%s..."' % (i + 1,message[:50]))

        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecryption.decryptMessage(key,encrypted)

            #If message doesn't match it exits

            if message != decrypted:
                    print('Mismatch with key %s and message %s' % (key, message))
                    print('Decrypted as: ' + decrypted)
                    sys.exit()

    print('Transposition cipher test passed')

if __name__ == '__main__':
    main()
