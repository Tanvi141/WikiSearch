#this parses the xml file, extracts raw contents of each doc, and sends it for processing
import xml.sax
from process import doc_to_ind
from indexer import write_to_disk

titles_total = 0
index_count = 0
out_dirname = ""
output_file = ""

class WikiDocParser(xml.sax.ContentHandler):
	lod = [{}, {}, {}, {}, {}, {}]
	sow = set()
	titles = {}
	global titles_total
	global out_dirname
	global output_file

	def __init__(self):
		self.title = ""
		self.text = ""
		self.titleflag = 0
		self.textflag = 0
		self.totaldocs = 0
		
	def startElement(self, lbl, attrs):
		if lbl == "title":
			self.title= ""
			self.titleflag = 1
		elif lbl == "text":
			self.text = ""
			self.textflag = 1
	
	def endElement(self, lbl):
		if lbl == "title": #page title
			self.titleflag = 0

		elif lbl == "text": #page content
			self.textflag = 0

		elif lbl == "page": #end of curr page
			global titles_total
			global index_count
			self.totaldocs += 1
			titles_total += 1

			title_ind = titles_total
			doc_to_ind(self.title, self.text, title_ind, self.lod, self.sow)
			self.titles[title_ind] = self.title

			if self.totaldocs %10 == 0:
				op = str(self.totaldocs)
				op += "\r"
				print(op, end="")
			
			if self.totaldocs % 10000 == 0:
				write_to_disk(self.lod, self.sow, out_dirname, "indexfile_" + str(index_count) + ".txt")
				write_titles(self.titles, out_dirname)
#				self.lod.clear()
				self.lod = [{}, {}, {}, {}, {}, {}]
				self.sow.clear()
				self.titles.clear()
				index_count += 1
		
		elif lbl == "mediawiki":	#end of the input file
				write_to_disk(self.lod, self.sow, out_dirname, "indexfile_" + str(index_count) + ".txt")
				write_titles(self.titles, out_dirname)
#				
	def characters(self, data):
		if self.titleflag == 1:
			self.title += data
		elif self.textflag == 1:
			self.text += data

def parse_doc(filename, passed_dirname, passed_output):
	global out_dirname
	global output_file
	global titles_total
	global index_count

	print("Titles so far", titles_total)
	
	out_dirname = passed_dirname
	output_file = passed_output

	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	parser.setContentHandler(WikiDocParser())
	parser.parse(open("%s"%(filename),"r"))
	
	index_count += 1

	return titles_total

def write_titles(titles, dirname):
	with open(dirname+"/titles.txt","a+") as f:
		for key in titles:
			f.write(str(key) + ":" + str(titles[key]) + "\n")
