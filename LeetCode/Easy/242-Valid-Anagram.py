import unicodedata
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        answer to the follow up question, what if the inputs contain Unicode characters, how would we handle this?

        so what are Unicode characters, Unicode itself is a standardized system that assigns a unique code (called code point) to every character in 
        every language and symbol set in the world. Covers way more than ASCII, that is just for English letters, digits and some symbols

        so the issue here is that for Unicode, some characters can have different byte representation even if they look the same, and so are hence not the same
        so we need to normalize the string into a consistent composition form, so that identical characters can pass the == check, since they are now the same when normalized
        we do the normalization using Python's unicodedata.normalize(form, string). 2 types of form, NFC -> composed form, and NFD -> decomposed form 
        we have to import unicodedata


        '''
        # so this is the solution when it contains Unicode characters

        s = unicodedata.normalize('NFC', s)
        t = unicodedata.normalize('NFC', t)

        return Counter(s) == Counter(t)


        # normal solution
        hashDict, checkDict = {}, {}
        for char in s:
            if char in hashDict:
                hashDict[char] += 1
            else:
                hashDict[char] = 1
        for check in t:
            if check in checkDict:
                checkDict[check] += 1
            else:
                checkDict[check] = 1
        if checkDict == hashDict: return True
        return False
    

        # another more optimized solution but also with hashmap
        # sHash = {}
        # for char in s:
        #     sHash[char] = sHash.get(char, 0)+1
        # for lett in t:
        #     sHash[lett] = sHash.get(lett,5)-1
        # for val in sHash.values():
        #     if val != 0:
        #         return False
        # return True