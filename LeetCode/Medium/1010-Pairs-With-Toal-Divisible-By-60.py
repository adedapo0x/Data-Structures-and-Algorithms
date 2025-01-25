class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        Approach here is to find the modulus operation of each song by 60. We find out that there are two possibilities. Either the elements
        are divisible by 60 or they are not. 
        '''
        mapCount = [0] * 60
        count = 0
        for n in time:
            mod = n % 60
            if mod == 0:
                count += mapCount[0]
            else:
                count += mapCount[60-mod]
            mapCount[mod] += 1
        return count


    # Bruteforce approach (results in TLE on LC)
    # Use two loops, check for each possible pair and count which sums are divisible by 60
    # TC: O(N^2), SC: O(1)