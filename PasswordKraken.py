''' 
urllib : http related libary
urllib.urlopen : open file from url
hashlib : hash algorithms to use in code
'''
from urllib.request import urlopen, hashlib

# Gets they type of hash from the user 
hash_type = input("Select a type of Hash: 1.MD5  2.SHA-1  3.SHA-256")

# Step 1: Request hashes to crack from the user 
hash_file_name=input("Enter the name of the .txt file that holds the hashes to crack: ")
# open the hash file provided by the user
sha1_hash_file = open(hash_file_name, "r")
# for loop to examine each hash in the user file
for current_hash in sha1_hash_file:
  crack_found = False
  current_hash = current_hash.rstrip()
  # turns the user hash to lowercase so that we can assume it is lowercase going forward
  current_hash = current_hash.lower()

# Step 2: Open our password wordlist
  LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

# Step 3: Choose a password from our password list from Step 2
  for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    #print("this is whats in guess", guess)

# Step 4: Hash the password chosen in Step 3
# Step 4.5: Depending on the hash chosen at first, use the necessary function

# MD5 Hashing
if (hash_type == 1) {
	# Need code for MD5
}
# SHA-1 Hashing
else if (hash_type == 2) {
	hashedGuess = hashlib.sha1(bytes(guess,'utf-8')).hexdigest()
    #print("this is whats in hashedGuess", hashedGuess)
}
# SHA-256 Hashing
else if (hash_type == 2) {
	# Need code for SHA-256

}
# User is trolling us
else {
	print("Incorrect Hash selected")
	quit()
}
    

# Step 5: Compare the hash generated from Step 4 to the current hash from the user being examined
    # 5.1 - If we find a match, print the successful password
    if hashedGuess == current_hash:
      # if match print ..
      crack_found = True
      print("The password is ", str(guess))
      break
    # 5.2 - If we don't find a match, jump back to Step 3 and choose another password from our wordlist
    #else:
      #print("Password guess ", str(guess), " does not match..trying next..")

# Step 6: If we do not find a match by the end of our password wordlist, print that a match was not found.
  if (crack_found == False):
    print("Password not in database, we'll get them next time.")
