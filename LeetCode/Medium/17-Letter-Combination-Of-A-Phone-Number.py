class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        We initially keep a dictionary to map the numbers to the letters they represent on the phone
        Approach here is to recursively go through each of the characters, starting from the first, and see all combinations that could be made for it, then
        go to the second possible element and repeat the same again and again

        Implementation-wise, we are more of actually going down depthwise to find all the possible combos that can work taking the first character before backtracking 
        and finding combinations that begin with the second character and so on

        TC: (n * 4^n) we get 4*n because the max amount of letters associated with a number is 4 e.g for 7 and 9. so say worst case scenario, we are given 99, there would have to be 
        16 combinations, so we have 4 not 3, and also the length of each combination is of length n so the time complexity would be (n * 4^n)
        SC: o(n) for extra space, but for output list, we get O(n * 4^n)

        Note that we are using a list and the join operation and not just a string because strings in Python are immutable and we would just be creating new strings on every 
        recursion and that is an expensive O(n) operation 
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