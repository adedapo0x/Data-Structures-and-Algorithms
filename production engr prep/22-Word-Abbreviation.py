'''
alid Word Abbreviation
A word can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
For example, internationalization can be written i12iz4n: i, then the 12 letters nternationali replaced by 12, then z, 
then the 4 letters atio replaced by 4, then n.

Given a word and a string abbr, decide whether abbr is a valid abbreviation of word. Two rules make invalid abbreviations: 
a number may not have a leading zero (01 is invalid, and so is 0, which would replace an empty substring), 
and the numbers must account for exactly the right number of letters, no more and no fewer. Digits that sit next to each other 
form one number (12 means twelve, never one then two).

Input format
Line 1: the string word (lowercase letters). Line 2: the string abbr (lowercase letters and digits).
Output format
Print true if abbr is a valid abbreviation of word, otherwise false.

Sample input
internationalization
i12iz4n
Expected output
true

'''

def validate_abbr(word, abbr):
    # approach is to use two ptrs to track both strs as we traverse 
    word_len, abbr_len = len(word), len(abbr)
    word_ptr, abbr_ptr = 0, 0
    
    while word_ptr < word_len and abbr_ptr < abbr_len:
        current_abbr_char = abbr[abbr_ptr]
        if current_abbr_char.isdigit():
            # if number starts with "01", abbr is invalid based on the problem statement
            if current_abbr_char == "0":
                return False
            num = ""
            while abbr_ptr < abbr_len and abbr[abbr_ptr].isdigit():
                num += abbr[abbr_ptr]
                abbr_ptr += 1
            word_ptr += int(num)
        else:
            if word[word_ptr] != abbr[abbr_ptr]:
                return False
            word_ptr += 1
            abbr_ptr += 1
    # we need to have processed everything on both strings to be able to return True
    # there should be no left overr characters in both
    return abbr_ptr == len(abbr) and word_ptr == len(word)
