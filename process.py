from Stemmer import Stemmer
from spacy.lang.en.stop_words import STOP_WORDS
stemmer = Stemmer('porter')

#tokenise
def tokenise(data_str):                                          
	tokenisedWords=re.findall("\d+|[\w]+",data_str)
	#tokenisedWords=[key.encode('utf-8') for key in tokenisedWords]
	return tokenisedWords

#remove all stop words and perform stemming
def stem_fold_stop(data_list):
	without_stop=[]
	for word in data_list:
		word = word.lower()
		word = stemmer.stemWord(word) 
		if word in STOP_WORDS:
			continue
		without_stop.append(word)
	return without_stop


