import Stemmer
import re
from nltk.corpus import stopwords 
stemmer = Stemmer.Stemmer('english')
stop_words = set(stopwords.words('english'))
from match import search_file

def blocks(files, size=65536):
	while True:
		b = files.read(size)
		if not b: break
		yield b

def get_total_docs(dirname):
	with open(dirname+"/titles.txt", "r",encoding="utf-8",errors='ignore') as f:
		return sum(bl.count("\n") for bl in blocks(f))
		
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

def id_to_title(dirname, doc_id):
	f =  open(dirname+"/titles.txt", "r")
	line = f.readline().strip('\n')
	while line:
		curr_id = int(line.split(":", 1)[0])
		if curr_id == doc_id:
			return  line.split(":", 1)[1]
		line = f.readline().strip('\n')
	return "NOT FOUND IN TITLES"

def query_parse(dirname, query_str):
	lbls = ['t','i', 'b','c','l','r']
	
	k_max= int(query_str.split(",")[0])
	query_string = query_str.split(",")[1]
	sp = query_string.split(':')
	candidate_docs = []
	scores = {}
	total_docs = get_total_docs(dirname)
#	print("total docs is", total_docs)
	if len(sp) == 1: #then is is a plain query
		toks = stem_and_stop(tokenise(lower_string(query_string)))
		for word in toks:
#			print("Posting list for:", word)
			temp_dict = search_file(dirname, word, '-', total_docs)
#			print(temp_dict)
	else:
		#print(sp)
		for i in range(1,len(sp)):
			field_letter = sp[i-1][len(sp[i-1])-1] #the last char
			words = sp[i]
			if i != len(sp)-1:
				words = words[:-2]
			for word in stem_and_stop(tokenise(lower_string(words))):
				if word != " ":
#					print("Searching for %s in %s"%(word, field_letter))
					temp_dict = search_file(dirname, word, field_letter, total_docs)
					for doc_id in temp_dict:
						if doc_id in scores:
							scores[doc_id] = scores[doc_id] + temp_dict[doc_id]
						else:
							scores[doc_id] = temp_dict[doc_id]
#					print(temp_dict)

	scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}
	cnt = 0
	for doc_id in scores:
		cnt += 1
		print(str(doc_id) +",", id_to_title(dirname, doc_id))
	while cnt < k_max:
		doc_id = random.randint(1, total_docs-2)	
		if doc_id not in scores:
			cnt += 1
			print(str(doc_id)+",", id_to_title(dirname, doc_id))
	
#	print(scores)


