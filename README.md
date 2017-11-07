# Article_Summarizer

## Final project for Intro to AI (COSC 4550) Fall 2017, University of Wyoming.

### Professor: Dr. Nick Cheney

Use the http://www.nltk.org/ package?

#### Preliminary Notes Taken 11/6/17

#### Paths this project can take:
Since I am only in an intro class and have no previous knowledge of natural language processing, this project can end up being a variety of things.
* An article classifier. Determines which category an article fits into ie. scientific, political, etc.
* An article summarizer -- summarizes using sentences from the actual article. Creates a heuristic? Text Extraction. (**This is the version I am leaning towards)
* An article summarizer -- summarizes by creating new sentences? Text Abstraction (*This is most likely out of the scope of this class and alloted time, but is something I definitely would like to pursue in the future)


#### Resources/examples/notes used for inspiration:

* Example of text summarizer that creates a one sentence summary of an article. 
https://www.youtube.com/watch?v=ogrJaOIuBx4
  * Uses Keras machine learning library (https://keras.io/)
  * 'Abstractive' method of summarizing. ie. the same way humans summarize
  
  1. Uses news article training set from mlg.ucd.ie/datasets/bbc.html
  2. Convert it to 'pickle' format -- converts it to a raw byte stream. (converts python object to character stream)
  3. Save data as a tuple comprising of 'heading', 'description', and 'keywords'.
  4. Split the text into individual words (a way to represent words numerically ie. word2vec or Glove )
    - word2vec: two layer neural net, pretrained neural net, takes word as input, produces vector as output
    - Glove: count based. --what this example uses
  5. Sequence to Sequence -- neural architecture
  6. Encoder and decoder network
  7. ...
  
* I found a project outline from another school to build an extraction based text summarizer. The document is included in the repo "HowToBuildATextSummarizerTutorial.docx"
* http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=2FE5724184FBAA48FFB7C96AA1362907?doi=10.1.1.471.1723&rep=rep1&type=pdf
  * This article talks about using sentence selection heuristics.
  * This research is almost exactly what I want to try to do.
  * https://arizona.pure.elsevier.com/en/publications/using-sentence-selection-heuristics-to-rank-text-segments-in-txtr
  
* http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.188.3982&rep=rep1&type=pdf

### More Concrete Ideas:

From the article above titled "Using Sentence-Selection Heuristics to Rank Text Segments in TXTRACTOR"

#### Methods for Identifying Sentences for Summaries:
1. word frequency
2. "cue phrases" https://arxiv.org/abs/cs/9609102 is a study on "Cue Phrase Classification Using Machine Learning"
3. title and heading words
4. sentence location

  ** or.... A combination of these methods!


#### Eduard Hovy: Reasearcher in NLP area
https://www.cs.cmu.edu/~hovy/


