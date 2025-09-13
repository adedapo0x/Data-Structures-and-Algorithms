class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        first = freq[s[0]]

        for val in freq.values():
            if val != first:
                return False

        return True
    

        # another way of checking the frequencies after creating the dict
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        vals = set(freq.values())

        return len(vals) == 1