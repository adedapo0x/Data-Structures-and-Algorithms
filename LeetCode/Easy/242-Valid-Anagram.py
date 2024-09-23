class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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