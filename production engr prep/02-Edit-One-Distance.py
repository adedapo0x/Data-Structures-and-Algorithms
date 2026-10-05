def editOneDistance(word1, word2):
    '''
    here we have cases to consider:
    1. if the length difference between the two words is greater than 1, then they cannot be one edit distance apart, so we can return False
    2. if the length difference is 1, so we can either insert a character into the shorter word or delete a character from the longer word,to check if they are now the same
    3. if the length difference is 0, then we can either replace a character in one of the words to make them the same

    here, we keep the longer word in longer and the shorter word in shorter so we know if the length difference is 1, we are only considering removing from the longer word

    the last return statement is for the case where the two words are the same except for the last character of the longer word,
    so we can just add a character to the shorter word to make them same or remove that extra character. We need that check there, because for us to get there that means we haven't seen any difference in the letters,
    and if it is that we have exactly the same word, we would return true which is not right.
    '''
    longer, shorter = word1, word2
    if len(word2) > len(word1):
        longer, shorter = word2, word1
        
    lengthDifference = len(longer) - len(shorter)
        
    if lengthDifference > 1:
        return False
    
    for i, char in enumerate(shorter):
        if char != longer[i]:
            if lengthDifference == 1:
                return longer[i+1:] == shorter[i:]
            if lengthDifference == 0:
                return longer[i+1:] == shorter[i+1:]
                
    return lengthDifference == 1