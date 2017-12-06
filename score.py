#score.py

""" This class calculates the score of each sentence and stores the score in 
an array in the index of the same sentence. """
 
class Score: 
    
    def __init__(self, num_sentences):
        self.num_sentences = num_sentences
        self.scores = [0] * num_sentences
        
    # Prints the scores of each sentence
    def get_scores(self):
        index = 0
        return self.scores

    # Updates the score of a sentence at a given index
    def update_score(self, index, score):
        self.scores[index] = self.scores[index] + score
        


class Segment_Score:
    """ Initializes another scores array holding the scores for each
        segment of the article.
    """
        
    def __init__(self, numsegs):
        self.num_segs = numsegs
        self.seg_scores = [0] * numsegs
       
    def update_seg_score(self, index, score):
        self.seg_scores[index] = self.seg_scores[index] + score
        
    def get_seg_scores(self):
        print "SEG SCORES"
        return self.seg_scores
        


        
