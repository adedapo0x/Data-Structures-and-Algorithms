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