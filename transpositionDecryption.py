#Transposition Cipher Decryption

import math, pyperclip

def main():
	myMessage = 'Cenoonommstmme oo snnio. s s c'
	myKey = 8

	plaintext = decryptMessage(myKey, myMessage)
	print(plaintext + '|')

def decryptMessage(key, message):
	#The number of columns in our transposition grid
	#Must form a rotated grid to decode message
	#To decode the key is the number of rows instead of the number
	#of columns
	numOfColumns = int(math.ceil(len(message) / float(key)))
	numOfRows = key

	#The number of shaded boxes in the last column to make sure the grid does
	#not have missing boxes and forms a complete grid multiple
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

	#Each string in plaintext represents a column in the grid:
	plaintext = [''] * numOfColumns
	column = 0
	row = 0

	for symbol in message:
		plaintext[column] += symbol
		column += 1 #point to the next column

		#If there are no more columns OR we're at a shaded box, go back
		#To the first column and the next row:
		if(column == numOfColumns) or (column == numOfColumns - 1 and
			row >= numOfRows - numOfShadedBoxes):
			column = 0
			row += 1

	return ''.join(plaintext)

#If transpositionDecrypt.py is run( instead of imported as a module)
#call the main() function

if __name__ == '__main__':
	main()
