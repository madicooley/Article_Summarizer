import nltk, string
from nltk.corpus import stopwords
from nltk.tokenize.texttiling import TextTilingTokenizer
import nltk.data
    

class Document_Segments:
    
    """ Uses the nltk package textiling to split a document into categories """
    
    def __init__(self, document):
        self.document = document
    
    # Segments document into topics via nltk package
    def run(self):
        segments = self.sent_tokenize()
	return segments
        
    def sent_tokenize(self):
        t = nltk.tokenize.TextTilingTokenizer()
        return t.tokenize(self.document)
    
    # Determines which sentences are in which segment for future lookup
    #def define():
        
