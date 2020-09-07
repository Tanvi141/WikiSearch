def log_index(dirname):
	dirname += "/index"
	tf = open(dirname+"/log.txt", 'r')
	line = tf.readline().strip('\n')
	ret = []	
	while line:
		word = line.split("=")[1]
		ret.append(word)
		line = tf.readline().strip('\n')
	return ret

def log_title(dirname):
	dirname += "/title"
	tf = open(dirname+"/log.txt", 'r')
	line = tf.readline().strip('\n')
	ret = []	
	while line:
		curr_id = int(line.split("=")[1].split(":")[0]) 
		ret.append(curr_id)
		line = tf.readline().strip('\n')
	return ret

def find_file(word, tok_track):
	l = 0
	r = len(tok_track)-1
	while l<=r:
		m = int((l+r)/2)
		if word < tok_track[m]:
			r = m - 1
		else:
			l = m + 1
	return l-1
