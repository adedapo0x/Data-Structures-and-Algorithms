class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        Approach here is to store all possible ways that a number can come as roman
        so we go beyond just I, V, X, L, C, D, M and include the anomalies such as CM, IV etc
        then we start from the end, say for the letter 3267, we want M first before we have CC, so we do just that
        start from the end of our list since that has the M and remove the 3000 from it, denote the M * how many times it appeared,
        we keep on doing this till we get to the start of the list, then we would have gotten all the values 

        TC: O(1), SC: O(1)
        '''
        romanAndInt = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
            ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], 
            ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]
        ]

        result = []
        for symbol, value in reversed(romanAndInt):
            if num // value:
                count = num // value
                result.append(symbol * count)
                num = num % value

        return "".join(result)


