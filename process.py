from nltk.stem import *
import re
from spacy.lang.en.stop_words import STOP_WORDS
stemmer = PorterStemmer()

#tokenise
def tokenise(data_str):                                          
	tokenisedWords=re.findall("\d+|[\w]+", data_str)
	#tokenisedWords=[key.encode('utf-8') for key in tokenisedWords]
	return tokenisedWords

#lowercase
def lower_string(data_str):
	return data_str.lower()

#remove all stop words and perform stemming
def stem_and_stop(data_list):
	without_stop=[]
	for word in data_list:
		word = stemmer.stem(word) 
		if word in STOP_WORDS:
			continue
		without_stop.append(word)
	return without_stop


#parse the title	
def get_title(data):
	pass

#getting the infobox
def get_infobox(data):
	infoboxes = []
	infoboxinds = []
	for m in re.finditer("{{infobox", data):
		start = m.start()
		ind = start + 4 #somewhere in the middle of the word "infobox"
		op = 2
		end = -1
		while ind < len(data)-1 and end == -1:
			if data[ind] == '{':
				print("open", end = "")
				op += 1
			elif data[ind] == '}':
				print("close", end ="")
				op -=1
				if data[ind+1] == '}' and op == 1:
					end = ind
			ind +=1
		if end != -1:
			print(start, end)
			infoboxes += tokenise(data[start:end])
			infoboxinds.append([start, end])
		
	return stem_and_stop(infoboxes), infoboxinds


#getting the references
def get_ref(data):
	refs = []
	for m in re.finditer(r'==\s*references\s*==', data):
		n = re.search(r'==[a-z ]*==', data[m.start()+5:])
		if n:
			refs = refs + tokenise(data[m.start():n.end()])
		else:
			refs = refs + tokenise(data[m.start():])
			break

	for m in re.finditer(r'<\s?ref[^\/>]*\/>', data):
		refs += tokenise(m[0])

	for m in re.finditer(r'<\s?ref[^\/>]*\>.*<\/\s?ref\s?>', data):
		refs += tokenise(m[0])
	
	return stem_and_stop(refs)
		
#getting the categories
def get_category(data):
	start = len("[[category:")
	cats = []
	beg = -1
	for m in re.finditer("\[\[category:.*\]\]", data):
		cats = cats + tokenise(m[0][start:-2])
		if beg == -1:
			beg = m.start()
	return stem_and_stop(cats), beg


#getting the external links	
def get_links(data, end):
	links = []
	m = re.search(r'==\s*external links\s*==', data)
	if m:
		if end != -1:
			links = stem_and_stop(tokenise(data[m.start():end]))
		else:
			links = stem_and_stop(tokenise(data[m.start():]))
		return links, m.start()
	else:
		return [], -1


#completely pre-process
def doc_to_ind(title, text, doc_id):
	text = lower_string(text)
	title = lower_string(title)
	print("ALL",text)
	get_title(title)
	lol, beg_of_cats = get_category(text)
	print("CATS", lol)
	lol, beg_of_links = get_links(text, beg_of_cats)
	print("LINKS", lol)
	lol1, lol2 = get_infobox(text)
	print("INFO", lol1)
	get_ref(text)

