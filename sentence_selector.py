#sentence_selector.py

from document import split_sentences, sentence_count, split_segments


def run(numsents, fil, scores, segscores):
    """ This function is what is called in order to selected the sentences 
        that will make it to the final summary.
        
        It selects from multiple 'segments' of the article in order
        to create a summary which captures all aspects of the original 
        document.
    """
    boundaries = create_segment_boundaries(fil)
    #numsents = get_number_sents(length, fil)
    final_sentences = select_sentences(boundaries, numsents, scores, fil)
    
    
def create_segment_boundaries(fil):
    """ Determines which index ranges correspond to each segment within
        the article.
        
        Returns an array comprised of pairs where each pair represents
        a lower and upper boundary for each topic segment of the article.
        Where the lower boundary is inclusive and the upper boundary is 
        exclusive. [lower, upper).
        
        If a sentence with index i falls within one of the ranges, that
        means it is within that segment.
    """
    
    segments = split_segments(fil)
    i = 0
    j = 0
    boundaries = [0] * len(segments)
    for seg in segments:
        lower = i
        sentences = split_sentences(seg)
        for sent in sentences:
            i += 1
        upper = i
        pair = (lower, upper)
        boundaries[j] = pair
        j += 1
        
    return boundaries


#def get_number_sents(length, fil):
    #""" This function determines the number of sentences that will be in
        #the summary based on the percentage specified by the user. 
    #"""
    #s = len(split_sentences(fil))
    #num = (float(length)/100) * s
    #return round(num)


def select_sentences(boundaries, numsents, scores, fil):
    """ This function take an array of tuples which contain the boundaries
        of topics. These boundaries are indexes within the array of sentences.
        Each boundary represents a range of indices within this array. It also 
        takes an integer called numsents which is the total number of sentences
        that should be included in the summary.
        
        This function returns an array of indices representing the final sentences
        to be included in the summary. 
    """
    #scores = heuristic.get_scores()
    #sentences = split_sentences(seg)
    
    #print boundaries
    #print scores
    sentences = 0
    sents = int(numsents)
    i = 0
    j = 0
    indices = [0] * sents
    for lower, upper in boundaries:
        lower_bound = lower
        upper_bound = upper
        
        maxx = 0
        while(lower_bound < upper_bound):
            value = scores[lower_bound]
            #print "value: ", i, " ",value
            if(value > maxx):
                maxx = i
            lower_bound += 1
            i += 1
        indices[j] = maxx
        if(j == sents -1): break
        j += 1
            
        
    #print indices
    
    #i = 0
    #j = 0
    #for lower, upper in boundaries:
        #lower_bound = lower
        #upper_bound = upper
        
        #maxx = 0
        #for score in scores:
            #if (i == upper_bound): break
            #value = scores[i]
            #print "value: ", i ," ", value
            #if(value > maxx):
                #maxx = i
            #i += 1
            
        #indices[j] = maxx
        #if(j == sents -1): break
        #j += 1
            
        
        
        
        
        
        
        
        
        
        