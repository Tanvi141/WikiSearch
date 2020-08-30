#this parses the indexfile
import os

#utility function for parsing the posting list
def get_field(field_letter, line):
	#use .split
	pass

#parses the stored line
def parse_line(line):
	s1 = line.split("=")
	return s1[0], s1[1]

#returns posting list for the word in the file
def search_file(dirname, query_word, field_letter): 
	lines = []
	for filename in os.listdir(dirname):
		with open("%s/%s"%(dirname,filename),"r") as f:
			lines = f.readlines()
	
		for line in lines:
			word, pl = parse_line(line)
			if word == query_word:
				return pl
		return "word not found!!"
