import nltk, string
from nltk.corpus import stopwords
from nltk.tokenize.texttiling import TextTilingTokenizer
import nltk.data
from nltk.tokenize.treebank import TreebankWordTokenizer

    

class Document_Segments:
    
    """ Uses the nltk package textiling to split a document into categories """
    
    def __init__(self, document):
        self.document = document
    
    def sent_tokenize(self, doc):
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        return tokenizer.tokenize
        #_word_tokenize = TreebankWordTokenizer().tokenize
        #return _word_tokenize(doc)
    
    #
    def run(self):
        doc = self.document
        tokens = self.sent_tokenize(doc)