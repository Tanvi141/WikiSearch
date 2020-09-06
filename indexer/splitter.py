import os

def split_files(dirname, split_val):
	infile = open(dirname+"/indexfile_0.txt","r")
	cnt = 1
	line = infile.readline().strip('\n')
	ind = 0

	of =  open(dirname+"/indfile"+str(ind) +".txt", 'w+')
	tf = open(dirname+"/log.txt", 'w+')
	tf.write(str(ind)+"="+line.split("=")[0] +"\n")
	
	while line:
		start_words = [line.split("=")[0]]
		of.write(line + '\n')
		cnt += 1
		line = infile.readline().strip('\n')
		
		if cnt % split_val == 0:
			of.close()
			print("here")
			of = open(dirname+"/indfile"+str(ind) +".txt", 'w+')
			ind += 1
			tf.write(str(ind)+"="+line.split("=")[0] +"\n")

	of.close()		
	tf.close()
