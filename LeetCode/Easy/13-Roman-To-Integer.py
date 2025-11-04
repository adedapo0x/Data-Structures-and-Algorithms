class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        Here we scan the string from left to right
        important to note that although the greatest ones are to be by the left before the smaller ones e.g for the number 523 we have DCCIII
        but there would be cases where a smaller value can come before a larger value like 92 where we have XCII, where X comes before C or 4 which is 
        IV where I comes before V, so we need to check for every value is there something larger than it one step to the right so we can account for it
        cos if we add them up like for IV, we would get 1 + 5 = 6 whereas it should be 4.

        so as we iterate through s, for each character at index i we check if what is after it is greater than it, if it is we subtract s[i] value from the total we have been
        building up, if it is not, we add the s[i] value to our total

        TC: O(1) this is because although we iterate through the entire string, it has a very finite bound, roman numerals can only grow up to 3999
        this is where we can represent it normally without using overlines or any thing else, so the number of roman characters we can possibly have worse case scenario is finite
        MMMCMXCIX

        SC: O(1) our hashmap size never grows beyond 7
        '''
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total

        