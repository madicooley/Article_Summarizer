from nltk import sent_tokenize
from sentence import Sentence

class Document:

    """This class creates a 'document' object"""

    def __init__(self, fil):
        self.fil = fil

    # This function splits an entire document up by sentence
    def split_file(self):
    
        doc = self.fil.read()
        sentences = sent_tokenize(doc)
        #print sent_tokenize(doc)
        return sentences
    
    # Calculates number of sentences in an array
    def sentence_count(self, sentences):
        #i = 0
        #for sent in sentences:
           # i += 1
        return len(sentences)
    
        
            



