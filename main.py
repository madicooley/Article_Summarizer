#!/usr/bin/env python

import re

def main():
    
    with open("test_article.txt", "r") as f:
        doc = f.read()

    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', doc)

    for sent in sentences:
        print(sent)
        print("")

    f.close()

if __name__ == "__main__":
    main()
