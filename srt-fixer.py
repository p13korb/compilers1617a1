
import sys
import re
import argparse
import datetime

parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
		regularexpression=re.compile(r'(?P<hours>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d+,\d+))
		
		
		sys.stdout.write(line)

		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --

