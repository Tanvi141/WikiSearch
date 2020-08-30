#this file takes the text and title of the doc and converts it into a series of lists, one list for each doc 
from preprocess import *
from indexer import lists_processing

#parse the title	
def get_title(data):
	toks = tokenise(data)
	return stem_and_stop(toks), len(toks)

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
				op += 1
			elif data[ind] == '}':
				op -=1
				if data[ind+1] == '}' and op == 1:
					end = ind
			ind +=1
		if end != -1:
			infoboxes += tokenise(data[start:end])
			infoboxinds.append([start, end])
		
	return stem_and_stop(infoboxes), infoboxinds, len(infoboxes)


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

#	for m in re.finditer(r'<\s?ref[^\/>]*\/>', data):
#		refs += tokenise(m[0])[2:]

#	for m in re.finditer(r'<\s?ref[^\/>]*\>.*<\/\s?ref\s?>', data):
#		refs += tokenise(m[0])[1:-1]   #from here can also remove https, url
	
	return stem_and_stop(refs), len(refs)
		
#getting the categories
def get_category(data):
	start = len("[[category:")
	cats = []
	beg = -1
	for m in re.finditer("\[\[category:.*\]\]", data):
		cats = cats + tokenise(m[0][start:-2])
		if beg == -1:
			beg = m.start()
	return stem_and_stop(cats), beg, len(cats)


#getting the external links	
def get_links(data, end):
	links = []
	m = re.search(r'==\s*external links\s*==', data)
	if m:
		if end != -1:
			toks = tokenise(data[m.start():end])											  
		else:
			toks = tokenise(data[m.start():])
		return stem_and_stop(toks), m.start(), len(toks)
	else:
		return [], -1, 0

#getting the body
def get_body(data, stop):
	toks = tokenise(data[:stop])
	return stem_and_stop(toks), len(toks)


#completely process, function to interface with parse.py
def doc_to_ind(title, text, doc_id, lod, sow):
	text = lower_string(text)
	title = lower_string(title)
	
	v = 0
	titl, v1 = get_title(title)
	v += v1
	cats, beg_of_cats, v1 = get_category(text)
	v += v1
	links, beg_of_links, v1 = get_links(text, beg_of_cats)
	v += v1
	infobox, lol2, v1 = get_infobox(text)
	v += v1
	refs, v1 = get_ref(text)
	v += v1
	body, v1 = get_body(text, beg_of_links)
	v += v1
		
	lists_processing([titl, infobox, body, cats, links, refs], lod, doc_id, sow)
	
	return v	
