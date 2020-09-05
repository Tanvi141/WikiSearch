import os

#utility function for parsing the posting list
def get_field(field_letter, line):
	#use .split
	pass

#parses the stored line
def parse_pl(pl):
	lbls = ['t','i','b','c','l','r']
	rev_lbs = lbls[::-1]
	
	temp_dict = {}
	for c in rev_lbs:
		res = pl.split(c)
		if len(res) != 1:
			temp_dict[c] = res[1]
		pl = res[0]
	return temp_dict

def merge_pl(pl1, pl2):
	lbls = ['t','i','b','c','l','r']
	dict1 = parse_pl(pl1)
	dict2 = parse_pl(pl2)
	print(dict1, dict2)	
	pl = ""
	for c in lbls:
		
		if c in dict1:
			pl += c
			pl += dict1[c]
			if c in dict2:
				pl += ","
				pl += dict2[c]
			continue
		
		if c in dict2:
			pl += c
			pl += dict2[c]
		
	return pl

def merge_once():
	pass

def merge_all_files():
	pass

print(merge_pl("t136426:1,136435:1i234:2,67758:34r135442:1,135497:1","b23:44l234:34,111:2r3443:4"))
