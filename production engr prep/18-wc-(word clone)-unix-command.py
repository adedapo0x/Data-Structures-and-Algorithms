'''
wc Clone with Top Words
wc is a unix command (word clone) that outputs three things
lines words bytes

lines - represents the number of newline characters
words - represents number of whitespaced separated values
bytes - total bytes in data

question as an extra part of after we print lines words bytes, we then want to print the top 5 most frequent words in the data given
'''

import heapq
from collections import Counter
def wc_clone_with_top_k(data):
    lines = data.count("\n")

    words = data.strip().lower().split()
    word_count = len(words)
    
    word_bytes = len(data.encode("utf-8"))
    
    print(f"{lines} {word_count} {word_bytes}")
    
    
    # second part
    word_freq = Counter(words)
    top_5_words = heapq.nlargest(5, word_freq.items(), key=lambda pair: (pair[1]))
    for word, freq in top_5_words:
        print(f"{word} {freq}")
    


