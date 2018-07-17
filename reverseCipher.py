#Reverse Cipher 
import time 
message = 'There should be secrets'
translated = ''
i = len(message) - 1
while i >= 0:
	translated = translated + message[i]
	i = i - 1
	
print(translated)
time.sleep(10)