import xml.sax

class WikiDocParser(xml.sax.ContentHandler):
	
	def __init__(self):
		self.title = ""
		self.text = ""
		self.titleflag = 0
		self.textflag = 0

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
			pass

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

