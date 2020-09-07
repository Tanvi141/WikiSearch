import os

def split_files(dirname, split_val, inputfile, outdir, flag):
	infile = open(dirname+"/"+inputfile,"r")
	
	dirname =dirname +"/" +outdir
	cnt = 1
	line = infile.readline().strip('\n')
	if flag==1:
		line = infile.readline().strip('\n') #the first line is space, so ignoring that
	ind = 0

	of =  open(dirname+"/indfile"+str(ind) +".txt", 'w+')
	tf = open(dirname+"/log.txt", 'w+')
	tf.write(str(ind)+"="+line.split("=")[0] +"\n")
	ind += 1
	while line:
		start_words = [line.split("=")[0]]
		of.write(line + '\n')
		cnt += 1
		line = infile.readline().strip('\n')
		
		if cnt % split_val == 0:
			of.close()
			print("here")
			of = open(dirname+"/indfile"+str(ind) +".txt", 'w+')
			tf.write(str(ind)+"="+line.split("=")[0] +"\n")
			ind += 1

	of.close()		
	tf.close()
