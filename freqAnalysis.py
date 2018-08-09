# Frequency Finder

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
    letterCount ={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
    'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
    'S': 0, 'T': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount

def getItemAtIndexZero(items):
    return items[0]

def getFrequencyOrder(message):
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter: #comparing the letter count
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter) #Adding to list if
            #same letter count
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find,reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

        #Tuple pairs (key, value) and then sort them
        freqPairs = list(freqToLetter.items())
        freqPairs.sort(key=getItemAtIndexZero, reverse=True)

        #Extract all the letters for the final string
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)
    matchScore = 0
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    for uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore

def main():
    myMessage = "This is a neat program"
    myMatchScore = englishFreqMatchScore(myMessage)
    print(myMatchScore)
    pass

if __name__ == '__main__':
    main()
