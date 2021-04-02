''' 
urllib : http related libary
urllib.urlopen : open file from url
hashlib : hash algorithms to use in code
'''
from urllib.request import urlopen, hashlib

#get hash from user to crack
sha1hash=input("Enter input the hash to crack : ")
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')


#guess from list
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
	print("this is whats in guess", guess)

	#hash the guessed password
	hashedGuess = hashlib.sha1(bytes(guess,'utf-8')).hexdigest()
	print("this is whats in hashedGuess", hashedGuess)

	#compare the hash user gave to guess
	if hashedGuess == sha1hash:

		#if match print ..
		#if doest, loop back
		print("The password is ", str(guess))
		quit()
	elif hashedGuess != sha1hash:
		print("Password guess ", str(guess), " does not match, ..trying next..")

#let user know we are at end of file
print("Password not in database, we'll get them next time.")
