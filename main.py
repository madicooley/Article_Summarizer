#!/usr/bin/env python

from document import Document
from score import Score
from doc_segmentor import Document_Segments

def main():
    
    f = open("test_article.txt", "r")

    #create document object
    doc = Document(f)
    sentences = doc.split_file()    
    num_sentences = doc.sentence_count(sentences)
    
    f.close()
    
    scores = Score(num_sentences)
    #scores.get_scores()
    
    segments = Document_Segments(doc)
    segments.run()
    


if __name__ == "__main__":
    main()
