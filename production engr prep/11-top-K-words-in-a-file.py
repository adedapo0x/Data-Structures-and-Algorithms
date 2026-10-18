'''
Question is to print the top k most frequent words in the file
'''

'''
Two approach to solving this
Approach 1: read the file content into a string, use regex to turn the string into individual words, then use a dictionary to count the frequency of each word. 
Finally, sort the dictionary by frequency and print the top k words.

Approach 2: using a heap. a minheap to be precise. after getting count, we then use a heap to iterate over the map using a minheap of size k to keep count of the words with the
highest frequencies. the minheap would always have at the root the word with the smallest count, so if we a see a more frequent word after, we then replace it

'''
from collections import Counter
import re



from collections import Counter
import re
import heapq

WORD_RE = re.compile(r"[a-z0-9']+")

def find_top_k_freq_words(filepath, k):
    '''
    approach using the heap
    nlargest here is a function that returns the k largest elements from the iterable, in this case, the counts.items() which is a list of tuples (word, count)

    for the error handling part: we use OSError as that covers every OS related problem such as I/o failure, missing files or permission issues
    opening a file is an OS work, open() is a syscall, so we cover for any of that and catch the error and raise it neatly
    the from at the end is to chain the error to the one we are raising so when debugging we can tell that the custom error we raised is due to e

    TC: O(N + MlogK) where N is the number of words in the file and M is the number of unique words and K is the number of top frequent words we want to find.
    SC: O(N + k)
    '''
    word_count = Counter()
    try:
        with open(filepath, "r") as file:
            for line in file:
                words = WORD_RE.findall(line.strip().lower())
                word_count.update(words)
    except OSError as e:
        raise OSError(f"Could not read {filepath}: {e}") from e
        
    top_k_words = heapq.nlargest(k, word_count.items(), key=lambda pair: pair[1])
    return top_k_words
        

    # this is building the heap manually, if we do not want to use the nlargest function
    heap = []
    for word, count in word_counts.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, word))
        else:
            if count > heap[0][0]:
                heapq.heapreplace(heap, (count, word))

    for count, word in sorted(heap, reverse=True):
        print(word)


def find_top_k_words(filepath, k):
    '''
    Sorting approach
    TC: O(N + MlogM) where N is the number of words in the file and M is the number of unique words.
    SC: O(N + M)
    '''
    with open(filepath, "r") as file:
        text = file.read().lower()
    words = re.findall(r"[a-z0-9']+", text)
    counts = Counter(words)
    top_words = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    for word, freq in top_words[:k]:
        print(word)