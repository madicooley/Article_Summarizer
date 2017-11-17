#!/usr/bin/env python

from doc_segmentor import Document_Segments
from heuristics import Heuristic

def main():
    
    f = open("test_article.txt", "r").read()
    
    #1. segments the article
    segments = Document_Segments(f)
    segments.run()
    
    #2. runs sentences through heuristics
    heuristic = Heuristic(f)
    scores = heuristic.get_scores()


if __name__ == "__main__":
    main()
