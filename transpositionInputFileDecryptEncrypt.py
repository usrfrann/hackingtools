# Transposition Cipher File Encrypt/Decrypt

import time, os, sys, transpositionDecryption, transpositionEncrypt

def main():

    inputFileName = 'frankenstein.txt'
    outputFileName = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'decrypt' # Set to 'encrypt' or 'decrypt'

    # If the input does not exist, the program terminates early:
    if not os.path.exists(inputFileName):
        print('The file %s does not exist. Quitting...' % (inputFileName))
        sys.exit()

    # If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFileName):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFileName))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file:
    fileObj = open(inputFileName)
    content = fileObj.read()
    fileObj.close() # Do not forget

    print('%sing...' % (myMode.title()))

    #Measure how long the encryption/decryption takes

    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecryption.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(),totalTime))

    # Write out the translated message to the output file:
    outputFileObj = open(outputFileName, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters.)' % (myMode, inputFileName, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFileName))

if __name__ == '__main__':
    main()


