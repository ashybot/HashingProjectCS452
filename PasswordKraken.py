# Step 1: Request hashes to crack from the user 
# ^ I think we can request 1 password hash for now, but we should eventually request a file of multiple password hashes.

# Step 2: Open our password wordlist (ex: rockyou.txt)
# ^ Eventually we should give the user the option to provide the wordlist theirselves.

# Step 3: Choose a password from our password list from Step 2

# Step 4: Hash the password chosen in Step 3

# Step 5: Compare the hash generated from Step 4 to all of the hashes provided by the user

# Step 6: Conditional statement for if we do or don't find a match
    # 6.1 - If we find a match, print the successful password
    # 6.2 - If we don't find a match, jump back to Step 3 and choose another password from our wordlist

# Step 7: If we do not find a match by the end of our password wordlist, print that a match was not found.
