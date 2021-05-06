#!/usr/bin/python
#MD5 cracker using HashLib

import time
import hashlib
import sys
import urllib2

#Start clock
start = time.time()

solution = str(sys.argv[1])
guess = " "
sol = "No Solution Found"

filename = urllib2.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt')

for line in filename:
	m = hashlib.md5()
	m.update(line[:-1])
	guess = m.hexdigest()

	if guess == solution:
		sol = line
		break

filename.close()

end = time.time()

t_time = str(round(end - start,3))
print "Total runtime was: ", t_time, " Seconds. Answer was: ", sol