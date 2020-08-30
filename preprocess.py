import Stemmer
import re
from spacy.lang.en.stop_words import STOP_WORDS
stemmer = Stemmer.Stemmer('english')

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
