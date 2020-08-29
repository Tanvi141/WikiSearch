#this parses the xml file, extracts raw contents of each doc, and sends it for processing
import xml.sax
from process import doc_to_ind
from indexer import write_to_disk

class WikiDocParser(xml.sax.ContentHandler):
	lod = [{}, {}, {}, {}, {}, {}]
	sow = set()

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
			self.totaldocs += 1
			doc_to_ind(self.title, self.text, self.totaldocs, self.lod, self.sow)
			if self.totaldocs %10 == 0:
				print("\r"+str(self.totaldocs))
			
	def characters(self, data):
		if self.titleflag == 1:
			self.title += data
		elif self.textflag == 1:
			self.text += data

def parse_doc(filename):
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	parser.setContentHandler(WikiDocParser())
	parser.parse(open("%s"%(filename),"r"))
	print("writing")
	write_to_disk(WikiDocParser.lod, WikiDocParser.sow, "indexfile")
