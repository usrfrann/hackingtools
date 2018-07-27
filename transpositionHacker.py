# Transposition Cipher Crack

import pyperclip, detectEnglish, transpositionDecryption

def main():
    myMessage = "Cenoonommstmme oo snnio. s s c"
    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to Hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        #pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print('Hacking...')
    print('Press (Ctrl-C)(on windows) or Ctrl-D (on macOS and Linux) to quit at any time')

    # Brute-force looping through every possible key
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = transpositionDecryption.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':
    main()