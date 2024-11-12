class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = {} 

        for ch in s:
            hashMap[ch] = hashMap.get(ch, 0) + 1 # gets count of each character in input string s
        
        count = [[] for i in range(len(s) + 1)] # bucket sort to hold elements with frequencies as indexes
        res = []

        for key, value in hashMap.items():
            count[value].append(key)   # Populates bucket array, elements that have same frequency are appended to inner array at same frequency

        for i in range(len(count) - 1, 0, -1): # forms an array to be joined by output
            for c in count[i]:
                res.append(c * hashMap[c])

        return "".join(res)
