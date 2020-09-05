#this file is the main file which calls the parsing file
from parse import *
import sys
import time
import os

t0 = time.time()
dir_output = sys.argv[2]
#stat_file = sys.argv[3]
dir_input = sys.argv[1]

try:
	os.mkdir(sys.argv[2])
	print("Files created  will be stored in newly created directory '%s'"%(sys.argv[2]))
except:
	print("Files created will be stored in pre-existing directory '%s'"%(sys.argv[2]))

what_fileind = 1
for filename in os.listdir(dir_input):
	print("parsing file %s"%(filename))
	what_filename = "indexfile" + str(what_fileind) + "_" 
	parse_doc(dir_input+"/"+filename, dir_output, what_filename)
	what_fileind += 1

t1 = time.time()

print("\nTime taken for parsing:",t1-t0,"secs")
