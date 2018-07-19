#WellAnEvovledCipher

message = 'ftu5Iu5Iy I5qo4q6Iyq55msqL'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456780 !?.'

for key in range(len(SYMBOLS)):
	translate = ''
	#Loop through each symbol in message:
	#for symbol in SYMBOLS:
	#	symbolIndex = SYMBOLS.find(symbol)
	#	translatedIndex = symbolIndex - key
	#
	#	# Handle the wraparound:
	#	if translatedIndex < 0:
	#		translatedIndex = translatedIndex + len(SYMBOLS)
	#
	#	# Append the decrypted symbol:
	#	translated = translated + SYMBOLS[translatedIndex]
	#
	#
	# Loop through each symbol in message:
		for symbol in message:
			if symbol in SYMBOLS:
				symbolIndex = SYMBOLS.find(symbol)
				translatedIndex = symbolIndex - key

				# Handle the wraparound:
				if translatedIndex < 0:
					translatedIndex = translatedIndex + len(SYMBOLS)

				# Append the decrypted symbol:
				translated = translated + SYMBOLS[translatedIndex]

			else:
				# Append the symbol without encryption/decrypting:
				translated = translated + symbol

			# Display every possible decryption:
			print('Key #%s: %s' % (key, translated))

    #IDE IED what grammar say you?
    #Yes tomorrow there is a tomorrow