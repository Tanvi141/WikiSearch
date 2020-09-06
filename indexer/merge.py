import os

#parses the posting list
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

def parse_line(line):
	s1 = line.split("=")
	return s1[0], s1[1]

def merge_two_files(file1, file2, outfile, dirname):
	f1 = open(dirname+"/"+file1, 'r')
    f2 = open(dirname+"/"+file2, 'r')
    of = open(dirname+"/temp.txt", 'w')
    line1 = f1.readline().strip('\n')
    line2 = f2.readline().strip('\n')
	
	while (line1 or line2):

		if !line2:
			of.write(line1 + '\n')
			line1 = f1.readline().strip('\n')
  		
		elif !line2:
			of.write(line2 + '\n')
			line2 = f2.readline().strip('\n')
 
		else:
			word1, pl1 = parse_line(line1)
			word2, pl2 = parse_line(line2)
        
			if word1 == word2:
				of.write(word1 + '=' + merge_pl(pl1,pl2) + '\n')
				line1 = f1.readline().strip('\n')
				line2 = f2.readline().strip('\n')
 		
			elif word1 < word2:
				of.write(line1 + '\n')
				line1 = f1.readline().strip('\n')

			else:
				of.write(line2 + '\n')
				line2 = f2.readline().strip('\n')
   
	f1.close()
	f2.close()
	of.close()

	os.remove(dirname+"/"+file1)
	os.remove(dirname+"/"+file2)
	os.rename(dirname+"/temp.txt", dirname+"/"+outfile))

def merge_all_files(out_dir):
	all_files = [name for name in os.listdir('.') if os.path.isfile(name)]
	total_files = len(all_files)

	while total_files > 1:
		i = 0
		while i*2 + 1 < total_files:
			file1 = "indexfile_"+ str(2*i) + ".txt"
			file2 = "indexfile_"+ str(2*i + 1) + ".txt"
			outfile = "indexfile_"+ str(i) + ".txt" 
			merge_two_files(file1, file2, outfile, out_dir)
			i += 1
		if totalfiles % 2 == 1:
			os.rename(out_dir+"/indexfile_"+str(2*i)+".txt", out_dir+"/indexfile_"+str(i)+".txt")
		total_files = i
		print("\rtotalfiles is %d"%(total_files))
