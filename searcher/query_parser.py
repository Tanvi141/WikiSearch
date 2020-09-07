import Stemmer
import re
import random
from binsrch import *
from nltk.corpus import stopwords 
stemmer = Stemmer.Stemmer('english')
stop_words = set(stopwords.words('english'))
from match import search_file

def get_total_docs(dirname):
	return 10000

#tokenise
def tokenise(data_str):                                          
	tokenisedWords=re.split(r'[^A-Za-z0-9]+', data_str)
	#tokenisedWords=[key.encode('utf-8') for key in tokenisedWords]
	return tokenisedWords

#lowercase
def lower_string(data_str):
	return data_str.lower()

#remove all stop words and perform stemming
def stem_and_stop(data_list):
	without_stop=[]
	for word in data_list:
		word = stemmer.stemWord(word) 
		if word in stop_words:
			continue
		without_stop.append(word)
	return without_stop

def id_to_title(dirname, doc_id, toks_title):
	dirname += "/title"
#	tf = open(dirname+"/log.txt", 'r')
#	line = tf.readline().strip('\n')

#	curr_id = int(line.split("=")[1].split(":")[0]) 
#	ind = -1
#print("world is", word)

#	while curr_id <= doc_id:
#		print(word, query_word, ind)
#		ind += 1
#	line = tf.readline().strip('\n')
	
#		if not(line):
#			break
#		curr_id = int(line.split("=")[1].split(":")[0]) 

#	tf.close()
	
#	print(doc_id, "in", ind, find_file(doc_id, toks_title))	
	ind = find_file(doc_id, toks_title)
	filename = dirname+"/indfile"+str(ind)+".txt"
	f = open("%s"%(filename),"r")
	line = f.readline().strip('\n')
	
	while line:
		curr_id = int(line.split(":", 1)[0])
		if curr_id == doc_id:
			return  line.split(":", 1)[1]
		line = f.readline().strip('\n')
	return "NOT FOUND IN TITLES"

def query_parse(dirname, query_str, tok_index, tok_title):
	lbls = ['t','i', 'b','c','l','r']
	
	k_max= int(query_str.split(",")[0])
	query_string = query_str.split(",")[1]
#	print(k_max, query_string)
	
	scores = {}
	total_docs = get_total_docs(dirname)
#	print("total docs is", total_docs)
	
	sp = query_string.split(':')
	#plain  query
	if len(sp) == 1: #then is is a plain query
		toks = stem_and_stop(tokenise(lower_string(query_string)))
		#print(toks)
		for word in toks:
			if word != " " and word != "":
				#print("Posting list for:", word)
				temp_dict = search_file(dirname, word, '-', total_docs, tok_index)
				#print(temp_dict)
				for doc_id in temp_dict:
					if doc_id in scores:
						scores[doc_id] = scores[doc_id] + temp_dict[doc_id]
					else:
						scores[doc_id] = temp_dict[doc_id]


	#field query
	else:
		#print(sp)
		for i in range(1,len(sp)):
			field_letter = sp[i-1][len(sp[i-1])-1] #the last char
			words = sp[i]
			if i != len(sp)-1:
				words = words[:-2]
			for word in stem_and_stop(tokenise(lower_string(words))):
				if word != " " and word != "":
#					print("Searching for %s in %s"%(word, field_letter))
					temp_dict = search_file(dirname, word, field_letter, total_docs, tok_index)
					for doc_id in temp_dict:
						if doc_id in scores:
							scores[doc_id] = scores[doc_id] + temp_dict[doc_id]
						else:
							scores[doc_id] = temp_dict[doc_id]
#					print(temp_dict)

	scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}
	ret_str = ""
	cnt = 0
	for doc_id in scores:
		cnt += 1
		ret_str += str(doc_id) +", "+ id_to_title(dirname, doc_id, tok_title)+"\n"
		if cnt >= k_max:
			return ret_str, k_max

	while cnt < k_max:
		doc_id = random.randint(1, total_docs-2)	
		if doc_id not in scores:
			cnt += 1
			ret_str += str(doc_id)+", "+ id_to_title(dirname, doc_id, tok_title)+"\n"
	
	return ret_str, k_max
#	print(scores)


