#this file is the main file which calls the parsing file
from query_parser import *
from binsrch import *
import sys
import time

tok_index = (log_index(sys.argv[1]))
tok_title = (log_title(sys.argv[1]))
with open("queries_op.txt", "w") as query_outfile:
	tq_total = 0
	query_infile = open("queries.txt", 'r')
	line = query_infile.readline().strip('\n')
	while line:
		tq_total+=1
		t0 = time.time()
		ret, kvalue = query_parse(sys.argv[1], line, tok_index, tok_title)
		query_outfile.write(ret)
		t1 = time.time()
		query_outfile.write(str(t1-t0)+", "+ str((t1-t0)/kvalue) + "\n\n")
		line = query_infile.readline().strip('\n')
