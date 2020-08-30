#this file is the main file which calls the parsing file
from query_parser import *
import sys
import time

t0 = time.time()
query_parse(sys.argv[1], sys.argv[2])
t1 = time.time()

print("\nTotal time taken:",t1-t0,"secs")
