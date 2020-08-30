#this file is the main file which calls the parsing file
from parse import *
import sys
import time

t0 = time.time()
parse_doc(sys.argv[1], sys.argv[2], sys.argv[3])
t1 = time.time()

print("\nTotal time taken:",t1-t0,"secs")
