#sentence_selector.py

from document import split_sentences, sentence_count, split_segments


def run(numsents, fil, sentscores, segscores):
    """ This function is what is called in order to selected the sentences 
        that will make it to the final summary.
        
        It selects from multiple 'segments' of the article in order
        to create a summary which captures all aspects of the original 
        document.
    """
    segments = split_segments(fil)
    sents = split_sentences(fil)
    boundaries = create_segment_boundaries(segments)
    ordered_sentscores = get_maxscore_ordering(sentscores, sents)
    ordered_segscores = get_maxscore_ordering(segscores, segments)
    final_sentences = select_sentences(boundaries, numsents, ordered_sentscores, ordered_segscores, fil)
    
    
def create_segment_boundaries(segments):
    """ Determines which index ranges correspond to each segment within
        the article.
        
        Returns an array comprised of pairs where each pair represents
        a lower and upper boundary for each topic segment of the article.
        Where the lower boundary is inclusive and the upper boundary is 
        exclusive. [lower, upper).
        
        If a sentence with index i falls within one of the ranges, that
        means it is within that segment.
    """
    
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


def select_sentences(boundaries, numsents, ordered_sentscores, ordered_segscores, fil):
    """ This function take an array of tuples which contain the boundaries
        of topics. These boundaries are indexes within the array of sentences.
        Each boundary represents a range of indices within this array. It also 
        takes an integer called numsents which is the total number of sentences
        that should be included in the summary.
        
        This function returns an array of indices representing the final sentences
        to be included in the summary. 
    """
    
    print boundaries, '\n'
    print ordered_sentscores, '\n'
    print ordered_segscores
       
    sentences = 0
    i = 0
    j = 0
    indices = [0] * numsents
    for lower, upper in boundaries:
        lower_bound = lower
        upper_bound = upper
        
        maxx = 0
        while(lower_bound < upper_bound):
            value = ordered_sentscores[lower_bound]
            #print "value: ", i, " ",value
            if(value > maxx):
                maxx = i
            lower_bound += 1
            i += 1
        indices[j] = maxx
        if(j == numsents -1): break
        j += 1
            

def get_maxscore_ordering(scores, size):
    """ """
    ordered = [0] * len(size)
    i = 0
    for score in scores:
        pair = (score, i)
        ordered[i] = pair
        i += 1
    return sorted(ordered, key=lambda x: x[0], reverse=True)
        
    
        
        
        
        
        
        
        
        
        
