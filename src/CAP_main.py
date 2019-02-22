
import nltk
from CAP_classes import ParseArticle

from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import PorterStemmer

'''sample_1 = "The wood-and-concrete frame of a mixed-use apartment complex is largely complete at 12803 Washington Boulevard in Culver City. The five-story building, called the Lucky Apartments, is being developed as a joint venture between James Suhr & Associates and Tooley Interests.  The podium-type structure will contain 37 apartments - including three for very low-income households - above 7,200 square feet of ground-floor retail space.The modern low-rise structure, designed by Pleskow Architects, will offer a mix of one-, two-, and three-bedroom dwellings, some of which will feature private roof terraces and balconies.  Renderings portray a contemporary five-story edifice.James Suhr & Associates and Tooley Interests have named their project for Elias Lucky Baldwin, an entrepreneur and real estate developer whose 19th-century land holdings eventually evolved into communities including Arcadia, Monrovia, Sierra Madre, and Baldwin Hills.  The former Baldwin Motel once stood at the site of the new apartment building.Completion of the Lucky is anticipated in Fall 2019."
stem_develop = ["develop", "developer", "developing", "developed"]

custom_tokenizer = PunktSentenceTokenizer(sample_1)
tokenized = custom_tokenizer.tokenize(sample_1)

def search_address():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i) # array of tokenized words
			tagged = nltk.pos_tag(words) # tag POS for each word
			 
			stdAddr = r"""std_adr: {<CD><NNP>+<IN.?><NNP>+}""" # standard address
			
			
			chunkParser = nltk.RegexpParser(stdAddr) # parse based on grammar
			addrChunks = chunkParser.parse(tagged) # chunked based on results 
			
			print(addrChunks)
			
		except Exception as e:
			print(str(e))'''

def main():
	a = ParseArticle("/home/jeremy/Desktop/CSE 516/CAPNLP/src/test.txt")
	a.proj_loc()

#main()
