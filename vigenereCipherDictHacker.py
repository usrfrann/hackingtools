#Vigenere Cipher Dictionary Hack

import vigenereCipher, pyperclip, detectEnglish

def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip()
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breakin:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText

def main():
    #ciphertext = """Tzx isnz eccjskg nfg lol mys bbqq I lxcz"""
    ciphertext = """Aapy Qaiwtwoc IFvicv hes p Qcmtxhs qaiwpqaixnmac, azkirxlr,
    cgnaxacpwcsi, pyh cdbayttg dgitcemsi."""
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')
    pass

if __name__ == '__main__':
    main()
