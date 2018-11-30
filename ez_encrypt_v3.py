import random
import os
import time

clear=lambda: os.system('cls')

def BS_startup():
	print('Welcome to eZ Encrypt v3. Initializing...')
	time.sleep(1)
	print('Bootstrapping encryption vector...')
	time.sleep(2)
	print('Collecting radio traffic for randomization...')
	time.sleep(3)
	print('Intialization Complete!')
	time.sleep(2)

BS_startup()

orig=input('Enter value to be randomized: ')
type(orig)

out=''.join(random.sample(orig,len(orig)))

pans=input("Would you like a password to be created to retrieve the original string?(y/n)")
type(pans)



if (pans == "y"):
	password=input("Enter a reversal key (password): ")
	type(password)
	clear()
	print(out)
	rev=input('Enter password to reverse encyption: ')
	type(rev)
	if (rev == password):
		print('Reversal in progress. Please wait...')
		time.sleep(3)
		print('The original string is: ' + orig)
		print('Done.')
	else:
		print('Password incorrect. Exiting...')
		exit()
else:
	if (pans == 'n'):
		print('Proceeding...')
		time.sleep(2)
		print(out)
		print('Done.')
		exit()
	else:
		return





##Dead code below##

#print(out)

#rev=input('Enter password to reverse encyption: ')
#

#if (rev == password):
#	print(orig)
#else:
#	print('Password incorrect. Exiting...')
#out=''.join(random.sample(orig,len(orig)))

