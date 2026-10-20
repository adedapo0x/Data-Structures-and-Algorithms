'''
find and count the number of emails in a file.
'''

import re
from collections import Counter

EMAIL_RE = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def find_emails(filepath):
    # TC: O(N) where N is the number of lines in the file
    # SC: O(M) where M is the number of unique emails in the file
    email_counter = Counter()
    with open(filepath, "r") as file:
        for line in file:
            email_counter.update(re.findall(EMAIL_RE, line))
    for email, count in email_counter.items():
        print(f"{email} has a count of {count}")