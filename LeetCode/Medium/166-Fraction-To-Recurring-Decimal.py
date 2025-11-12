class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        The logic here is to basically model long division
        we also need to check for some edgecases, we are guaranteed that denominator is never 0, so there is no risk of division by zero error
        things to check:
        - if numerator is 0, the answer is automatically "0"
        - if one of the values are negative, that means the answer is going to start with negative symbol, so we append that into our fraction list if
        that is the case, we have to explicitly check for this that only one is negative, but for the case of both being negative, we do nothing since answer would be positive.
        
        then there is the case of if it divides cleanly without a decimal point behind. we get the integer division and append to fraction list,
        if there is no remainder, we have our answer, and we can simply return our answer

        but if there is a remainder, we need to check the decimal part, we append . to begin,
        also we need a lookup hashmap in order to detect recurring decimals, so once a remainder repeats itself, we know the decimal is going to be 
        recurring and we need to place that recurring part in () and we check for that each time.

        now if we have not previously seen that remainder, we give its position in our hashmap, multiply remainder by 10 in a bid to see if we can divide now, similar to what is done
        in long division, then try the division again, we append that to our decimal building, take remainder again from that if it exists, if the remainder wasn't zero, we continue till it becomes
        zero or we detect recurring decimals

        TC: O(N) where N is the number of digits in the repeating decimal, so the loop goes for about O(N) time
        SC: O(N) to store distinct remainders in the lookup hashmap and we also use fraction list, so linear space
        
        '''
        if numerator == 0:
            return "0"

        fraction = []
        if (numerator < 0) != (denominator < 0):
            fraction.append("-")

        dividend = abs(numerator)
        divisor = abs(denominator)

        fraction.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(fraction)

        fraction.append(".")
        lookup = {}
        while remainder != 0:
            if remainder in lookup:
                fraction.insert(lookup[remainder], "(")
                fraction.append(")")
                break

            lookup[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // divisor))
            remainder %= divisor

        return "".join(fraction)


        