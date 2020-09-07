#this parses the indexfile
import os
import math 


def get_tf_idf(pl, total_titles, wt):
	docs_here = pl.split(",")	
	idf = math.log(total_titles / len(docs_here))
	dict_ret = {}

	for entry in docs_here:
		temp = entry.split(":")
		doc_id = temp[0]
		tf = math.log(1+int(temp[1]))
		dict_ret[int(doc_id)] = tf*idf*wt

	return dict_ret

#parses the posting list
def parse_pl(pl, field_letter):
	lbls = ['t','i','b','c','l','r']

	rev_lbs = lbls[::-1]
	
	temp_dict = {}
	for c in rev_lbs:
		res = pl.split(c)
		if len(res) != 1:
			temp_dict[c] = res[1]
		pl = res[0]
#	return temp_dict
	
	ret = ""
	if field_letter == '-':
		for c in temp_dict:
			ret += temp_dict[c]
	
	else:
		ret = temp_dict[field_letter]
	
	return ret


#parses the stored line
def parse_line(line):
	s1 = line.split("=")
	return s1[0], s1[1]

#returns posting list for the word in the file
def search_file(dirname, query_word, field_letter, total_docs): 
	dirname += "/index"	
	tf = open(dirname+"/log.txt", 'r')
	line = tf.readline().strip('\n')
	word = line.split("=")[1] 
	ind = -1
#print("world is", word)

	while word <= query_word:
#		print(word, query_word, ind)
		ind += 1
		line = tf.readline().strip('\n')
	
		if not(line):
			break
		word = line.split("=")[1]

	tf.close()
	
#	print(query_word, "in", ind)

	wts = {	't': 10,'i': 7 ,'b': 2, 'c': 8,'l': 5 ,'r': 3, '-': 1}
	filename = dirname+"/indfile"+str(ind)+".txt"
	f = open("%s"%(filename),"r")
	line = f.readline().strip('\n')
	
	while line:
		word, pl = parse_line(line)
		if word == query_word:
			return get_tf_idf(parse_pl(pl, field_letter), total_docs, wts[field_letter])
		
		line = f.readline().strip('\n')
	
	return {}
