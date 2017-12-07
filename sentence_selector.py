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
    #ordered_sentscores = get_maxscore_ordering(sentscores, sents)
    ordered_segscores = get_maxscore_ordering(segscores, segments)
    final_sentences = select_sentences(boundaries, numsents, ordered_segscores, sentscores, segments)
    print_summary(final_sentences, sents)
    
    
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


def select_sentences(boundaries, numsents, ordered_segscores, sentscores, segments):
    """ This function take an array of tuples which contain the boundaries
        of topics. These boundaries are indexes within the array of sentences.
        Each boundary represents a range of indices within this array. It also 
        takes an integer called numsents which is the total number of sentences
        that should be included in the summary.
        
        This function returns an array of indices representing the final sentences
        to be included in the summary. 
    """
    #print ordered_segscores
    #print sentscores
    #print boundaries
       
    sentences = 0
    i = 0
    indices = [-1] * numsents
    
    #for weight, index in ordered_segscores:
    while( sentences != numsents ):
        weight, index = ordered_segscores[i]
        bound = boundaries[index]
        first = bound[0]
        second = bound[1]
        maxx = -10
        value = 0
        while(first < second):
            s = sentscores[first]
            if ( first not in indices ): 
                if(s > maxx):
                    maxx = s
                    value = first
            first += 1
        indices[sentences] = value
        sentences += 1
        i += 1
        if (sentences == len(ordered_segscores)):
                i = 0
    
    return indices


def get_maxscore_ordering(scores, size):
    """ Returns an array consisting of pairs that correspond to 
        the weight of the segment or sentence and the index. 
        
        This function orders the highest weighted setences/segments
        first, and the least weighted last. 
    """
    ordered = [0] * len(size)
    i = 0
    for score in scores:
        pair = (score, i)
        ordered[i] = pair
        i += 1
    return sorted(ordered, key=lambda x: x[0], reverse=True)
        
    
def print_summary(sent_indices, sents):
    """ This function prints the actual summary. """
    sort = sorted(sent_indices, key=int)
    i = 0
    for ind in sort:
        print sents[ind]
        
        
        
        
        
        
