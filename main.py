#!/usr/bin/env python

from document import Document
from score import Score
from doc_segmentor import Document_Segments

def main():
    
    f = open("test_article.txt", "r").read()

    #1. create document object
    doc = Document(f)
    sentences = doc.split_file()    
    num_sentences = doc.sentence_count(sentences)
    
    #f.close()
    
    scores = Score(num_sentences)
    #scores.get_scores()
    
    #2. segments the article
    segments = Document_Segments(f)
    segments.run()
    
    #3. runs sentences through heuristics
    


if __name__ == "__main__":
    main()
