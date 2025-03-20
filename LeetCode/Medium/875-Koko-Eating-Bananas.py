class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Optimal solution. to get minimum eating rate, we have to check from lowest rate possible which would be 1 up until the highest rate it could
        possibly be, which is the maximum element in the pile array. This is because if we look at it, h (time given) cannot be lesser than length of pile array
        so it makes sense that if we take maximum element and try it as our k, if h should be less than piles.length(), she's never going to be fast enough since she can only
        eat one pile per hour. 
        so we need to check for the values between 1 and max(piles) for the minimum value k can be, the optimal way is to use a binary search.
        so if we find a time that works, we check if there is a lesser time that also works and repeat till our binary search loop condition is invalid
        TC: O(log(max(piles)).N) where N is the size of the piles array and we have log(max(piles)) since we're basically doing a binary search on a range of 1 to maxValue hence the log
        '''

        small, high = 1, max(piles)
        k = high
        while small <= high:
            mid =(small + high) // 2
            timeTaken = 0
            for n in piles:
                timeTaken += math.ceil(n / mid)
            if timeTaken <= h:
                k = min(mid, k)
                high = mid - 1
            else:
                small = mid + 1
        return k


        # Bruteforce solution follows similar thoughtprocess except that to check from 1 to maxValue we are using a linear search. so we are checking
        # every number in the range until we get to the first number in the range that it's possible to have Koko finish eating.