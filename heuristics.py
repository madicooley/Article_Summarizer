#heuristics.py

from document import split_sentences, sentence_count, split_segments
from score import Score

HEURONE_WEIGHT = 0.10
HEURTWO_WEIGHT = 0.05

class Heuristic:

    def __init__(self, fil):
        self.fil = fil  
        self.sentences = split_sentences(self.fil)
        self.num_sentences = sentence_count(self.sentences)
        self.scores = Score(self.num_sentences)
        #self.document = Document_Segments(self.fil)
        self.segments = split_segments(self.fil)
        
            
    # returns the scores array. Called by main
    def get_scores(self):
        self.run_all()    
        return self.scores.get_scores()

    # runs all of heuristics
    def run_all(self):
        self.heuristic_one()
        self.heuristic_two()

    def heuristic_one(self):
        """ This function takes a document and splits it by topic.
        
            It weights sentences towards the beginning of a paragraph more
            than the sentences towards the end of the paragraph since
            most articles are written to where the beginning sentences
            are more information heavy.

            The total heurstic value for all of the sentences combined
            for each segment in the article is about 0.10. It never
            fully reaches 0.10 though, and is often times much less
            ~0.75.  
            
            Updates the scores array.
        """
        i = 0  # index of each sentence
        for seg in self.segments:
            sentences = split_sentences(seg)
            j = 0
            weight = HEURONE_WEIGHT
            for sents in sentences:
                #print j, sents
                w = weight / 2
                print "WEIGHT ", i, " : ", w
                self.scores.update_score(i, w);

                weight = w
                j += 1
                i += 1
    
    def heuristic_two(self):

        """  This function finds all sentences that are quotes and 
             adds a penalty to these sentences. Quotes should probably
             (in my opinion) not be included in summaries. 
            
            Updates the scores array.
        """
        #sentences = split_sentences(self.fil)

        i = 0  # index of each sentence
        for sents in self.sentences:
            if('"' in sents):
                #print i,sents
                self.scores.update_score(i, -HEURTWO_WEIGHT)
            i += 1
    









