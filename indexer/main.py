#this file is the main file which calls the parsing file
from parse import *
import sys
import time
import os

t0 = time.time()
try:
	os.mkdir(sys.argv[2])
	print("Files created  will be stored in newly created directory '%s'"%(sys.argv[2]))
except:
	print("Files created will be stored in pre-existing directory '%s'"%(sys.argv[2]))

parse_doc(sys.argv[1], sys.argv[2], "indexfile.txt", sys.argv[3])
t1 = time.time()

print("\nTotal time taken:",t1-t0,"secs")
