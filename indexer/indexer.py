#this file takes lists of words in every section, and indexes them

def list_to_dict(l, d, doc_id):
	for word in l:
		if word in d:
			if doc_id in d[word]:
				d[word][doc_id] += 1
			else:
				d[word][doc_id] = 1 
		else:
			d[word] = {}
			d[word][doc_id] = 1


def lists_to_set(lol, sow):
	for lis in lol:
		for word in lis:
			sow.add(word)


def lists_processing(lol, lod, doc_id, sow): #list of dicts, list of lists, set of words
	for i in range(len(lol)):
		list_to_dict(lol[i], lod[i], doc_id)
	
#	for word in lol[5]:
#		try:
#			lod[2][word][doc_id] -= 1 #removing overlaps between the ref and body
#		except:
#			print("err")
	lists_to_set(lol, sow)


def write_to_disk(lod, sow, dirname, filename):
	all_words = sorted(sow)
	lbls = ['t','i', 'b','c','l','r']
	with open("%s/%s"%(dirname,filename),'w') as f:
		for word in all_words:
			f.write(word+'=')
			for i in range(6):
				flag = 0
				# print("\n", i)
				# print(lod)
				if word in lod[i]:
					f.write(lbls[i])
					for doc_id in lod[i][word]:
						if flag == 1: 
							f.write(",")
						else:
							flag = 1
						f.write(str(doc_id)+":"+str(lod[i][word][doc_id]))
			f.write("\n")
				
