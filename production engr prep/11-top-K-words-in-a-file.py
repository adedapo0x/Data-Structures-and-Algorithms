'''
Question is to print the top k most frequent words in the file
'''

'''
Two approach to solving this
Approach 1: read the file content into a string, use regex to turn the string into individual words, then use a dictionary to count the frequency of each word. 
Finally, sort the dictionary by frequency and print the top k words.

'''
from collections import Counter
import re

def find_top_k_words(filepath, k):
    '''
    TC: O(N + MlogM) where N is the number of words in the file and M is the number of unique words.
    SC: O(N + M)
    '''
    with open(filepath, "r") as file:
        text = file.read().lower()
    words = re.findall(r"[a-z0-9']+", text)
    counts = Counter(words)
    top_words = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    for word in top_words[:k]:
        print(word[0])