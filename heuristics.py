#heuristics.py

from document import split_sentences, sentence_count
from score import Score
from doc_segmentor import Document_Segments

class Heuristic:

    def __init__(self, fil):
        self.fil = fil  
        num_sentences = sentence_count(self.fil)
        self.scores = Score(num_sentences)
	      
	    
    # returns the scores array. Called by main
    def get_scores(self):
        self.run_all()    
        return self.scores.get_scores()

    # runs all of heuristics
    def run_all(self):
        self.heuristic_one()
        #heuristic_two()

	""" This function takes a document and splits it by topic and not
        just paragraph.
	    It weights sentences towards the beginning of a paragraph more
	    than the sentences towards the end of the paragraph since
	    most articles are written to where the begginning paragraphs
	    are more information heavy.  
	    
	    Updates the scores array.
	"""
    def heuristic_one(self):
        s = Document_Segments(self.fil)
        segments = s.run()

        for seg in segments:
            print seg 
            print '\n\n'
            sentences = split_sentences(seg)
            i = 0
            for sents in sentences:
                print i, sents
                print '\n'
                i += 1
        return 1
