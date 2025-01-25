class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        TC: O(N), SC: O(1), since we are using an arry of fixed size (60) doesn't change with change in length of the input.
        Approach here is to find the modulus operation of each song by 60. We find out that there are two possibilities. Either the elements
        are divisible by 60 or they are not. So we keep an array of size 60 (ie with indexes from 0 to 59). For every element, their modulus falls between 0 to 59,
        and we use this array to keep count, reason I'm not using an hashmap is to avoid key error. 
        So if the modulus is zero (value divisible by 60), we check if there is already another one divisible that we've encountered before through our count array, 
        then we increment our count variable by the amount already previously there at index 0
        But if the element is not divisible by 60, ie the modulus is not zero, to get what second value would make the sum of both divisible by 60, the sum of the modulus of both have to be equal to 60,
        so if we have an element with modulus x, to check if we already have an occurence of the second element needed to make their sum divisible, we do 60 - x, gives us the other modulus needed, and then we check
        for it occurence then add the value to our count variable.
        So basically the mapCount array I used here, the indexes denotes the modulus and the values denote the amount of elements with that modulus
        Whether or not the value is divisible or not, we have to increase the occurence of it in the count array after before we move on to the next element
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