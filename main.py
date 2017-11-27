#!/usr/bin/env python

import argparse
#from doc_segmentor import Document_Segments
from heuristics import Heuristic

# Method to get arguments from command line
def get_args():
    
    parser = argparse.ArgumentParser(description='Summarize an article.')
    
    parser.add_argument('-f', "--file", action='store',
                        help="File to be Summarized.", required=True)
    
    parser.add_argument('-l', '--length', action='store',
                        help="Lenght of summary in %. (ie. 20 )", required=True)
    
    parser.add_argument('-h', '--help', required=False)

    args = vars(parser.parse_args())

    return args

def main():
    
    #args = get_args()
    #print args
    
    f = open("test_article.txt", "r").read()
    
    #1. segments the article
    #segments = Document_Segments(f)
    #segments.run()
    
    #2. runs sentences through heuristics
    heuristic = Heuristic(f)
    scores = heuristic.get_scores()
    
    print scores


if __name__ == "__main__":
    main()
