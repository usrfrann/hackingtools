message = 'ftu5Iu5Iy I5qo4q6Iyq55msqL'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456780 !?.'

# loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            symbolIndex = LETTERS.find(symbol) # get the number of the symbol
            symbolIndex = symbolIndex - key

            # handles wrap-around if index is 26 or larger or less than 0
            if symbolIndex < 0:
                symbolIndex = symbolIndex + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[symbolIndex]

        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))