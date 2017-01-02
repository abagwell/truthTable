'''
This is a python3 scripts that draws a simple truth table for either coin flips or die rolls.

A coin is obviously 2 sides: Heads (H) and Tails (T)

A die has 6 sides (1, 2, 3, 4, 5, 6)

'''

#!/ur/bin/python

import sys

'''
Function Name: usage()
Description: this function evaluates the arguments passed in the command line. If the arguments are 
invalid in length or value, usage instructions are displayed to the user
'''

def usage():

	message = "Usage: python3 truthTable.py [-c | -d] [-f | -nf]" #just update the usage message here

	if len(sys.argv) != 3:
		print(message)
		sys.exit()
	
	elif (sys.argv[1] != '-c' and sys.argv[1] !='-d') or (sys.argv[2] != '-f' and sys.argv[2] != '-nf'):
		print(message) 
		sys.exit()

'''
This function runs when coins are used

'''

def coinOption(fairness):
	print("With Coins")

'''
This function runs when dice are used

'''

def diceOption(fairness): 
	print("With die")


def main():

	usage()

	if sys.argv[1] == '-c':
		coinOption(sys.argv[2])

	else:
		diceOption(sys.argv[2])

	print("Program Finished...")

if __name__ == '__main__':
	main()