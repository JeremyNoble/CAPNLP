
import nltk
from nltk.tokenize import PunktSentenceTokenizer

sample_1 = open("test.txt")
sample_2 = open("test.txt")

custom_tokenizer = PunktSentenceTokenizer(sample_1)
tokenized = custom_tokenizer.tokenize(sample_2)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i) # array of tokenized words
			tagged = nltk.pos_tag(words) # tag each word with its part of speech identifier
			 
			chunkGram = r"""Chunk: {<NNP.?>*}"""
			
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
			
			print(chunked)
			
			
			
			
			
			
			
			
			
			
			
			
			
	except Exception as e:
		print(str(e))
		
process_content()

