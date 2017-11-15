

""" This class calculates the score of each sentence and stores the score in 
an array in the index of the same sentence. """
 
class Score: 
    
    def __init__(self, num_sentences):
        self.num_sentences = num_sentences
        self.scores = [0] * num_sentences
        
    # Prints the scores of each sentence
    def get_scores(self):
        index = 0
        for score in self.scores:
            print "score ", index, ": ", score
            index += 1
        