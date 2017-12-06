#heuristics.py

from document import split_sentences, sentence_count, split_segments
from score import Score, Segment_Score

HEURONE_WEIGHT = 0.10
HEURTWO_WEIGHT = 0.05

class Sentence_Heuristic:

    def __init__(self, fil):
        self.fil = fil  
        self.sentences = split_sentences(self.fil)
        self.num_sentences = sentence_count(self.sentences)
        self.scores = Score(self.num_sentences)
        self.segments = split_segments(self.fil)
        
            
    # returns the scores array. Called by main
    def get_scores(self):
        self.run_all()    
        return self.scores.get_scores()

    # runs all of heuristics
    def run_all(self):
        self.heuristic_one()
        self.heuristic_two()
        

########## Sentence Heuristics ############

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
                #print "WEIGHT ", i, " : ", w
                self.scores.update_score(i, w)

                weight = w
                j += 1
                i += 1
    
    def heuristic_two(self):
        """  This function finds all sentences that are quotes and 
             adds a penalty to these sentences. Quotes should probably
             (in my opinion) not be included in summaries. 
            
            Updates the scores array.
        """

        i = 0  # index of each sentence
        for sents in self.sentences:
            if('"' in sents):
                self.scores.update_score(i, -HEURTWO_WEIGHT)
            i += 1
            
            

SEG_HEURONE_WEIGHT = 0.20
SEG_HEURTWO_WEIGHT = 0.10

class Segment_Heuristic:            

    def __init__(self, fil, sumsents):
        self.fil = fil
        self.sumsents = sumsents
        self.segments = split_segments(self.fil)
        self.seg_scores = Segment_Score(len(self.segments))
        
        
    # returns the scores array. Called by main
    def get_segscores(self):
        self.run_allseg()    
        return self.seg_scores.get_seg_scores()

    # runs all of heuristics
    def run_allseg(self):
        self.segment_heur_one()
        self.segment_heur_two()
        
        
######### Segment Heuristics ############
        
    def segment_heur_one(self):
        """ This function finds the introduction segments and
            the conclusion segments of an article and gives them
            and higher weight.
        """
        self.seg_scores.update_seg_score(0, SEG_HEURONE_WEIGHT)
        self.seg_scores.update_seg_score(len(self.segments)-1, SEG_HEURONE_WEIGHT)
        
        
    def segment_heur_two(self):
        """ This function finds segments that only consist of of
            one sentence (NOTE:: maybe make this 2 in the future??)
        """
        j = 0
        for seg in self.segments:
            i = 0
            sentences = split_sentences(seg)
            for sent in sentences:
                i += 1
            if(i < 2):
                self.seg_scores.update_seg_score(j, -SEG_HEURTWO_WEIGHT)
            j += 1
        
    









