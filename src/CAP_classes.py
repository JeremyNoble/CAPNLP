
import nltk
import re

from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import PorterStemmer
from nltk import ChunkParserI

class ParseArticle:
	
	Tagged = []
	
	# public methods
	
	# parameterized default constructor
	'''
	When instantiating an object, pass the name of the file
	which you would like to parse
	'''
	def __init__(self, filepath):
		self.parse_corp(filepath)
	
	# Initial Parser
	'''
	Parse the supplied text through the default constructor, 
	tag the POS then set the respective private variable
	'''
	def parse_corp(self, filepath):
		
		with open(filepath, "r") as fin:
			for sent in nltk.sent_tokenize(fin.read()):
				words = nltk.word_tokenize(sent) # array of tokenized words
				tagged = nltk.pos_tag(words) # tag POS for each word
				self.Tagged += tagged # add each tokenized sentenced to Tagged
				
				
	
	#def proj_name(): 
		
	def proj_loc(self):
			 
		stdAddr = r"""std_adr: {(<CD>+<NNP>+<,>?<IN>?<NNP>+)<CC>?(<CD>?<NNP>+<,>?<IN>?<NNP>?)?}""" # standard address
		
		
		addrParser = nltk.RegexpParser(stdAddr) # parse based on regex
		addrChunks = addrParser.parse(self.Tagged) # chunked based on results
		
		#addrChunks.draw() # draw the shallow tree
		
		for subtree in addrChunks.subtrees(filter=lambda t: t.label() == 'std_adr'):
			# print the noun phrase as a list of part-of-speech tagged words
			print(subtree)
		
	#def proj_dev(): 
		
	#def proj_arch(): 
		
	#def proj_lend(): 
		
	#def proj_cont(): 
		
	#def proj_scope():
		


def main():
	a = ParseArticle("/home/jeremy/Desktop/CSE 516/CAPNLP/src/test_addresses.txt")
	s = a.proj_loc ()
	print(s)

main()
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
