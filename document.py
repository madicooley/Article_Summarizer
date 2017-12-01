#document.py

import nltk, string
from nltk.corpus import stopwords
from nltk.tokenize.texttiling import TextTilingTokenizer
import nltk.data
from nltk import sent_tokenize


""" These functions use the nltk package textiling to split 
    a document into categories
"""


def split_sentences(fil):

    """ This function splits an entire document up by sentence.

    sent_tokenize uses an instance of PunktSentenceTokenizer 
    from the nltk. tokenize.punkt module. This instance has already 
    been trained on and works well for many European languages. 
    So it knows what punctuation and characters mark the end of 
    a sentence and the beginning of a new sentence. """

    sentences = sent_tokenize(fil)
    return sentences
    
# Calculates number of sentences in an array
def sentence_count(sentences):
    return len(sentences)

# Segments document into topics via nltk package
def split_segments(fil):
    t = nltk.tokenize.TextTilingTokenizer()
    segments = t.tokenize(fil)
    return segments
        
            



