class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        Approach here is to use divide and conquer, since we know that the 2^10 can be split into 2^5 and when we multiply it by itself we get the original question
        then split again to 2^2, multiply by itself, again and again, so basically what we are doing is, we break down the problem into subproblems and as we return we multiply by
        the value by itself.

        in our recursion, our base case is when n = 0, so anything raised to the power of 0 is 1, so we return 1. another case is if the input x is 0, we can 
        simply return 0, doesn't matter what n is here. In our splitting, we also have to be careful of how we split odd powers, say we have 2 ^ 5, splitting into two, gives 2 ^ 2 in two places,
        but that amounts to just 2 ^ 4, we still need to multiply by x, in this case, 2, to get back the original value of 2 ^ 5

        be mindful of negative powers too, we do not care about them in our recursion, and so we use abs, when we want to split power, raised to -5 and raised to 5 is the same,
        only that after we get the final answer, we do 1/res if the power was negative.

        TC: O(logN) since I am splitting power by 2, each time. where n is 
        '''
        def findPowerOf(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = findPowerOf(x, abs(n) // 2) # gets rid of negative sign in power
            res = res * res
            return x * res if n % 2 != 0 else res # checks for odd power, have to make up for it by multiplying with x one more time

        res = findPowerOf(x, n)
        return res if n >= 0 else 1/res # after we have gotten the actual value, then if negative power, we then do 1/res