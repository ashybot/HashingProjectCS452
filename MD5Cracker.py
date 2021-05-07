#!/usr/bin/python
#MD5 cracker using HashLib

import time
import hashlib
import sys
from urllib.request import urlopen
#import codecs


#Get hased MD5 input from user
password = input("Input hashed password: ")
password = password.lower()
password = password.rstrip()

#Open filename from url
#filename = urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt')
filename = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

passes = range(100)

for i in passes:

	start = time.time()

	for guess in filename.split('\n'):
		hashedGuess = hashlib.sha256(bytes(guess,'utf-8')).hexdigest()
		#hashedGuess = getattr(hashlib, 'md5')(bytes(guess)).hexdigest()
	

		if hashedGuess == password:
			#print("The password is: ", str(guess))
			#print(i)
			end = time.time()
			t_time = str(round(end - start,2))
			print(t_time)
			
			
			#print ("Total runtime was: ", t_time)
			break

	#elif hashedGuess != password:
	#	print("Password guess: ", str(guess), " does not match, trying next.")

#Password not found
#print("Password not found")
#end = time.time()
#t_time = str(round(end - start,2))
#print ("Total runtime was: ", t_time)







