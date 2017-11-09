#!/usr/bin/env python

from document import Document

def main():
    
    f = open("test_article.txt", "r")

    #create document object
    doc = Document(f)
    doc.split_file()    
    
    f.close()

if __name__ == "__main__":
    main()
