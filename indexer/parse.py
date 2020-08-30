#this parses the xml file, extracts raw contents of each doc, and sends it for processing
import xml.sax
from process import doc_to_ind
from indexer import write_to_disk

tokens_total = 0

class WikiDocParser(xml.sax.ContentHandler):
	lod = [{}, {}, {}, {}, {}, {}]
	sow = set()
	global tokens_total

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
			global tokens_total
			self.totaldocs += 1
			tokens_total += doc_to_ind(self.title, self.text, self.totaldocs, self.lod, self.sow)
			if self.totaldocs %10 == 0:
				op = str(self.totaldocs)
				op += "\r"
				print(op, end="")
			
	def characters(self, data):
		if self.titleflag == 1:
			self.title += data
		elif self.textflag == 1:
			self.text += data

def parse_doc(filename, output_file1, output_file2):
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	parser.setContentHandler(WikiDocParser())
	parser.parse(open("%s"%(filename),"r"))
	print("writing")
	
	write_to_disk(WikiDocParser.lod, WikiDocParser.sow, output_file1)
	print(tokens_total)
	with open("%s"%(output_file2),"w") as f:
		f.write(str(tokens_total))
		f.write("\n")
		f.write(str(len(WikiDocParser.sow)))
