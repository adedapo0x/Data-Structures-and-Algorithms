'''
Top K Error Types
An on-call engineer wants to know which kinds of errors are happening most. 
You are given log lines of the form timestamp LEVEL type, where LEVEL is something like INFO, WARN or ERROR. 
Only lines whose level is ERROR count. Group them by type and report the K most frequent types.
'''

from collections import Counter
import heapq

def top_k_error_types(filename, k):
    # TC: O(NlogK), SC: O(N + k)
    error_count = Counter()
    with open(filename, "r") as file:
        for line in file:
            _, level, type_of_error = line.split()
            if level == "ERROR":
                error_count[type_of_error] += 1
    top_k_errors = heapq.nlargest(k, error_count.items(), key=lambda pair:pair[1])
    for error, freq in top_k_errors:
        print(f"{error} - {freq}")