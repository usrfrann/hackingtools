# Vigenere Cipher Hacker

import itertools, re
import vigenereCipher, pyperclip, freqAnalysis, detectEnglish

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_KEY_LENGTH = 16
NUM_MOST_FREQ_LETTER = 4
SILENT_MODE = False
NONLETTERS_PATTERN = re.compile('[^A-Z]')
message1 ="THEDOGANDTHECATISOUTTHEBAG"


def main():
    ciphertext = """Aapy Qaiwtwoc IFvicv hes p Qcmtxhs qaiwpqaixnmac, azkirxlr,
    cgnaxacpwcsi, pyh cdbayttg dgitcemsi.""" #Brute Force time
    hackedMessage = hackVigenere(ciphertext)
    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to Hack Encryption.')
    pass

def findRepeatSequencesSpacings(message):
    #Goes though the message finding any 3 to 5 letter sequences that are repeated
    #Returns a dict with the keys of the sequence and values of a list of spacings

    #use a regular expression to remove non-letters from the message
    message = NONLETTERS_PATTERN.sub('', message.upper())

    #Compile a list of seqLen-letter sequence found in the message:
    seqSpacings = {} # Keys are sequences; values are lists of int spacings.
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            #Determine what the sequence is and store it in seq:
            seq = message[seqStart:seqStart + seqLen]
            #Look for this sequence in the rest of the message:
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    #Found a repeated sequence
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] # Initialize blank list.
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings

def getUsefulFactors(num):
    #Returns a list of useful factors
    # getUsefulFactors(144) returns [2,3,4,6,8,9,12,16]

    if num < 2:
        return []

    factors = [] # The list of factors found.

    #When finding factors, you only need to check up to the MAX_KEY_LENGTH
    for i in range(2, MAX_KEY_LENGTH + 1):
        if num % i == 0:
            factors.append(i)
            otherFactor = int(num / i)
            if otherFactor < MAX_KEY_LENGTH + 1 and otherFactor != 1:
                factors.append(otherFactor)
    return list(set(factors)) #Uses set to remove duplicate factors

def getItemAtIndexOne(x):
    return x[1]

def getMostCommonFactors(seqFactors):
    #First, get a count of how many times a factor occurs in seqFactors
    factorCounts = {}   #Key is a factor; value is how often it occurs.

    #seqFactors keys are sequences; values are lists of factors of the spacings.
    #spacings. seqFactors has a value like {'GFD': [2,3,4,6,9,12,23,36,46,69,92,
    #138,207}
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1

    factorsByCount = []

    for factor in factorCounts:
        if factor <= MAX_KEY_LENGTH:
            #factorsByCount is a list of tuples: (factor, factorCount).
            #factorByCount has value like [(3, 497), (2,487)....]
            factorsByCount.append((factor,factorCounts[factor]))
    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

    return factorsByCount

def kasiskiExamination(ciphertext):
    repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)
    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))

    factorsByCount = getMostCommonFactors(seqFactors)
    allLikelyKeyLengths = []
    for twoIntTuple in factorsByCount:
        allLikelyKeyLengths.append(twoIntTuple[0])

    return allLikelyKeyLengths

def getNthSubkeysLetters(nth, keyLength, message):
    #Returns every nth letter for each keyLength set of letters in text.
    #getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'
    #Use a regular expression to remove non-letters from the message.
    message = NONLETTERS_PATTERN.sub('', message)

    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)

def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
    #Determine the most likely letters for each letter in the key:
    ciphertextUp = ciphertext.upper()
    allFreqScores = []
    for nth in range(1, mostLikelyKeyLength + 1):
        nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertextUp)
        #FreqScore is a list of tuples like letter and English Freq match score
        #[<letter>, <Eng. Freq. match score>), ...]
        freqScores = []
        for possibleKey in LETTERS:
            decryptedText = vigenereCipher.decryptMessage(possibleKey, nthLetters)
            keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
            freqScores.append(keyAndFreqMatchTuple)
        freqScores.sort(key=getItemAtIndexOne, reverse=True)
        #Example of some of the allFreqScores =[[('A',9), ('E', 5), ('O', 4), ('P', 4)],
        #[('S', 10), ('D', 4), ('G', 4), ('H',4)]]
        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTER])

    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
            #Use i + 1 so the first letter is not called the "0th" letter:
            print('Possible letters for letter %s of the key: ' % (i + 1), end='')
            for freqScore in allFreqScores[i]:
                print('%s ' % freqScore[0], end ='')
            print() # Print a newline

    #Try every combination of the most likely letters for each position in the key
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTER),repeat=mostLikelyKeyLength):
        #Create a possible key from the letters in allFreqScores:
        possibleKey = ''
        for i in range(mostLikelyKeyLength):
            possibleKey += allFreqScores[i][indexes[i]][0]
        if not SILENT_MODE:
            print('Attempting with key: %s' % (possibleKey))
        decryptedText = vigenereCipher.decryptMessage(possibleKey, ciphertextUp)

        if detectEnglish.isEnglish(decryptedText):
            origCase = []
            for i in range (len(ciphertext)):
                if ciphertext[i].isupper():
                    origCase.append(decryptedText[i].upper())
                else:
                    origCase.append(decryptedText[i].lower())
            decryptedText = ''.join(origCase)

            #Check with user to see if the key has been found:
            print('Possible encryption hack with key %s:' % (possibleKey))
            print(decryptedText[:200])
            print()
            print('Enter D if done, anything else to continue hacking')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

def hackVigenere(ciphertext):
    allLikelyKeyLengths = kasiskiExamination(ciphertext)
    if not SILENT_MODE:
        keyLengthStr = ''
        for keyLength in allLikelyKeyLengths:
            keyLengthStr += '%s ' % (keyLength)
        print('Kasiski examinaation results say the most likely key lengths are: ' + keyLengthStr + '\n')
        hackedMessage = None
        for keyLength in allLikelyKeyLengths:
            if not SILENT_MODE:
                print('Attempting hack with key length %s (%s possible keys)...'
                % (keyLength, NUM_MOST_FREQ_LETTER ** keyLength))
            hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
            if hackedMessage != None:
                break

    #If none of the key lengths found using Kasiski examination worked, start brute-forcing
    if hackedMessage == None:
        print('Unable to hack message with likely key length. Brute forcing key length')
    for keyLength in range(1, MAX_KEY_LENGTH + 1):
        if not SILENT_MODE:
            print('Attempting hack with key length %s (%s possible keys)...' %
            (keyLength, NUM_MOST_FREQ_LETTER ** keyLength))
        hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
        if hackedMessage != None:
                break
        return hackedMessage

if __name__ == '__main__':
    main()
