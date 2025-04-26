class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        We initially keep a dictionary to map the numbers to the letters they represent on the phone
        Approach here is to recursively go through each of the characters, starting from the first, and see all combinations that could be made for it, then
        go to the second possible element and repeat the same again and again
        Implem
        '''

        mapping =  {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def backtrack(indx, temp):
            if len(temp) == len(digits):
                res.append("".join(temp))
                return

            for c in mapping[digits[indx]]:
                temp.append(c)
                backtrack(indx + 1, temp)
                temp.pop()

        if digits:
            backtrack(0, [])
        return res