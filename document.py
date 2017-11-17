#document.py

# ** import nltk.data
from nltk import sent_tokenize

def split_sentences(fil):

    """ This function splits an entire document up by sentence.

    sent_tokenize uses an instance of PunktSentenceTokenizer 
    from the nltk. tokenize.punkt module. This instance has already 
    been trained on and works well for many European languages. 
    So it knows what punctuation and characters mark the end of 
    a sentence and the beginning of a new sentence. """

    sentences = sent_tokenize(fil)
        #print sent_tokenize(doc)
    return sentences

    # This function splits an entire document up by paragraph
def split_paragraphs():
        #sentences = paragraph_tokenize(self.fil)
        #print sent_tokenize(doc)
    return sentences
    
    # Calculates number of sentences in an array
def sentence_count(fil):
    sentences = split_sentences(fil)
        #i = 0
        #for sent in sentences:
           # i += 1
    return len(sentences)


    
        
            



