#this file is the main file which calls the parsing file
from parse import *
import sys
import time
import os
from merge import *
from splitter import *

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
docs_so_farrr = 0
for filename in os.listdir(dir_input):
#	break
	print("parsing file %s"%(filename))
	what_filename = "indexfile" + str(what_fileind) + "_" 
	docs_so_farrr = parse_doc(dir_input+"/"+filename, dir_output, what_filename)
	what_fileind += 1

t1 = time.time()

print("\nTime taken for parsing:", t1-t0, "secs")
#exit(0)
t0 = time.time()
merge_all_files(dir_output, 1)
t1=time.time()
print("\nTime taken for merging:", t1-t0, "secs")


t0 = time.time()
os.mkdir(sys.argv[2]+"/index")
split_files(dir_output, 100000, "indexfile_0.txt", "index", 1)
t1=time.time()
print("\nTime taken for splitting", t1-t0, "secs")


t0 = time.time()
os.mkdir(sys.argv[2]+"/title")
split_files(dir_output, 10000, "titles.txt", "title", 0)
t1=time.time()
print("\nTime taken for splitting titles", t1-t0, "secs")


