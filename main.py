#!/usr/bin/env python

import argparse
from heuristics import Heuristic
from sentence_selector import run

# Method to get arguments from command line
def get_args():
    
    parser = argparse.ArgumentParser(description='Summarize an article.')
    
    parser.add_argument("-f", "--file", action='store',
                        help="File to be Summarized.", required=True)
    
    parser.add_argument("-l", "--length", action='store', type=int,
                        help="Length of summary in percentage. (ie. 20 ). Default is 20 percent of original article.", required=False)

    args = parser.parse_args()
    return args

def main():
    
    args = get_args()
    print args
    
    #f = open("test_article.txt", "r").read()
    f = open(args.file, "r").read()
    
    # run sentences through heuristics
    heuristic = Heuristic(f)
    scores = heuristic.get_scores()
    
    # run scores array through the sentence selector to create summary
    # creates a summary of length args.length or 20 % default.
    if args.length:
        summary = run(args.length, f) 
    else:
        summary = run(20, f) 
    
    print scores


if __name__ == "__main__":
    main()
