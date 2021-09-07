import sys
import string
from sklearn.feature_extraction import stop_words


stops = set(stop_words.ENGLISH_STOP_WORDS)
# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
            if words not in stop_words:
                print '%s\t%s' % (word, "1")
