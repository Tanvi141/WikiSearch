import Stemmer
import re
from spacy.lang.en.stop_words import STOP_WORDS

stemmer = Stemmer.Stemmer('english')
from match import search_file

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
		if word in STOP_WORDS:
			continue
		without_stop.append(word)
	return without_stop


def query_parse(filename, query_string):
	lbls = ['t','i', 'b','c','l','r']
	
	sp = query_string.split(':')
	if len(sp) == 1: #then is is a plain query
		toks = stem_and_stop(tokenise(lower_string(query_string)))
		for word in toks:
			print("Posting list for:", word)
			print(search_file(filename, word, '-'))

	else:
		#print(sp)
		for i in range(1,len(sp)):
			field_letter = sp[i-1][len(sp[i-1])-1] #the last char
			words = sp[i]
			if i != len(sp)-1:
				words = words[:-2]
			for word in stem_and_stop(tokenise(lower_string(words))):
				if word != " ":
					print("Posting list for:", word)
					print(search_file(filename, word, field_letter))

