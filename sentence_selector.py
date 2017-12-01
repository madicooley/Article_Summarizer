#sentence_selector.py

from document import split_sentences, sentence_count, split_segments


def run(length, fil):
    """ This function is what is called in order to selected the sentences 
        that will make it to the final summary.
        
        It selects from multiple 'segments' of the article in order
        to create a summary which captures all aspects of the original 
        document.
    """
    boundaries = create_segment_boundaries(fil)
    numsents = get_number_sents(length, fil)
    
    
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


def get_number_sents(length, fil):
    """ This function determines the number of sentences that will be in
        the summary based on the percentage specified by the user. 
    """
    s = len(split_sentences(fil))
    num = (float(length)/100) * s
    return round(num)
        
        
        
        
        
        
        
        
        
        
        
        
        
        