

""" This function takes a document and splits it by paragraphs.
    It weights sentences towards the beginning of a paragraph more
    than the sentences towards the end of the paragraph since
    most articles are written to where the begginning paragraphs
    are more information heavy.  
    
    returns: an array of weights where the index corresponds
    to the index of the sentence within the article.
"""
def heurisic_one(doc):
    