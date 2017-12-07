#heuristics.py

from document import split_sentences, sentence_count, split_segments, remove_stopwords
from score import Score, Segment_Score
from sentence_selector import create_segment_boundaries

HEURONE_WEIGHT = 0.10
HEURTWO_WEIGHT = 0.20
HEURTHREE_WEIGHT = 0.10


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
        self.heuristic_three()
        

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
            
            
    def heuristic_three(self):
        """ This function determines the relevancy of each sentence to the overall 
            subject of the article. It gets a dictionary which contains the frequency
            of words that are not stop words within the article. 
            
            It then compares the words in the frequency table to the words in the sentence.
            If the sentence contains words that are in the table, it's score is increase.
            
            The more words a sentence has that are 'relevant' the higher its score will be.
        """
        freqtable = remove_stopwords(self.fil)
        i = 0
        for sent in self.sentences:
            value = 0
            for wordval in freqtable:
                if wordval[0] in sent.lower():
                    value = value + HEURTHREE_WEIGHT
            value = value / len(sent)   #so longer sentences arent favored over shorter sents
            self.scores.update_score(i, value)
            i += 1
            
            
            
            

SEG_HEURONE_WEIGHT = 0.20
SEG_HEURTWO_WEIGHT = 0.10
SEG_HEURTHREE_WEIGHT = 0.10

class Segment_Heuristic:            

    def __init__(self, fil, sumsents, sent_scores):
        self.fil = fil
        self.sent_scores = sent_scores
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
        self.segment_heur_three()
        
        
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
            
            
    def segment_heur_three(self):
        """ This function penalizes segments where no sentences have a score
            greater than zero. """
        i = 0
        boundaries = create_segment_boundaries(self.segments)
        for bound in boundaries:
            first = bound[0]
            second = bound[1]
            maxx = 0
            while(first < second):
                s = self.sent_scores[first]
                first += 1
                if(s > maxx):
                    maxx = s
            if(maxx <= 0):
                self.seg_scores.update_seg_score(i, -SEG_HEURTHREE_WEIGHT)
            i += 1
    
    









