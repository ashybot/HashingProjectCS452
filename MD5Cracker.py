#!/usr/bin/python
#MD5 cracker using HashLib

import time
import hashlib
import sys
from urllib.request import urlopen
#import codecs

#Start clock


#solution = str(sys.argv[1])
#guess = " "
#sol = "No Solution Found"

#Get hased MD5 input from user
password = input("Input hashed MD5 password: ")
password = password.lower()
password = password.rstrip()

#Open filename from url
#filename = urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt')
filename = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

start = time.time()

for guess in filename.split('\n'):
	hashedGuess = hashlib.md5(bytes(guess,'utf-8')).hexdigest()
	#hashedGuess = getattr(hashlib, 'md5')(bytes(guess)).hexdigest()
	

	if hashedGuess == password:
		print("The password is: ", str(guess))

		end = time.time()
		t_time = str(round(end - start,3))
		print ("Total runtime was: ", t_time)
		quit()

	elif hashedGuess != password:
		print("Password guess: ", str(guess), " does not match, trying next.")

print("Password not found")
end = time.time()
t_time = str(round(end - start,3))
print ("Total runtime was: ", t_time)

'''
for line in filename:
	m = hashlib.md5()
	m.update(line[:-1])
	guess = m.hexdigest()

	if guess == solution:
		sol = line
		break

'''

#filename.close()



