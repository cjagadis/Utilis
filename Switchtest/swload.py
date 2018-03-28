'''Load Test Switcher
   1. Start a Switcher instance and use a random port
   2. Create 3 or more input URLs and one or more output URLS
   3. Call the Switcher directly using Python Telnet 
   4. Randomly send Commands
   5. Count the number of instances/streams
   6. Report the performance statistics
'''

import requests
import argparse
import logging as log

parser = argparse.ArgumentParser()
		  
parser.add_argument('-d', '--debug',
	help="print debugging statements",
	action="store_const", dest="loglevel", const=log.DEBUG,
	default=log.WARNING,
)
parser.add_argument('-v', '--verbose',
	help="verbose",
	action="store_const", dest="loglevel", const=log.INFO,
)
args = parser.parse_args()
		       
log.basicConfig(level=args.loglevel, format='%(asctime)s - %(levelname)s" - %(message)s')
			 
log.info("main:swload")


