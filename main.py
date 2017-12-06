#!/usr/bin/env python

import argparse
from heuristics import Sentence_Heuristic, Segment_Heuristic
from document import split_sentences
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


def get_number_sents(length, fil):
    """ This function determines the number of sentences that will be in
        the summary based on the percentage specified by the user. 
    """
    s = len(split_sentences(fil))
    num = (float(length)/100) * s
    return int(round(num))


def main():
    
    args = get_args()
    print args
    
    #f = open("test_article.txt", "r").read()
    f = open(args.file, "r").read()
    
    # run sentences through heuristics
    heuristic = Sentence_Heuristic(f)
    scores = heuristic.get_scores()
    
    # run scores array through the sentence selector to create summary
    # creates a summary of length args.length or 20 % default.
    if args.length:
        numsents = get_number_sents(args.length, f)
        seg_heur = Segment_Heuristic(f, numsents)
        segscores = seg_heur.get_segscores()
        print segscores
        summary = run(numsents, f, scores, segscores)
    else:
        numsents = get_number_sents(20, f)
        seg_heur = Segment_Heuristic(f, numsents)
        segscores = seg_heur.get_segscores()
        summary = run(numsents, f, scores, segscores) 
        


if __name__ == "__main__":
    main()
