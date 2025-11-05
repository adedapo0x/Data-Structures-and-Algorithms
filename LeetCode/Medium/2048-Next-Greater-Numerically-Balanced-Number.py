class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        '''
        The approach here is to try to compute the balanced numbers and see which is immediately greater than it using backtrack function
        the hashmap is used in building the numbers since each digit d must occur d times

        the backtrack function takes in num (the input given), current (the number we are building), and count (the amount of digits we are looking for)
        so when count is 0, we have the number of digits we are looking for, this is our base case, we then have to check that the hashmap is in order ie freq is either 0 (completely used up)
        or digit would be equal to freq (not used), if it doesn't satisfy the condition, that means only part as been used, we can't have that, so we return 0
        else we return current as our ans if it is greater than num cos in our generating, we might end up generating balanced number less than num, if so we return 0 in that case also

        now for the backtracking part, we take a number, by decrementing its count, explore with it while building our current using the * 10 + digit trick, and decrement the amount of 
        digits we need in count, if we return we need to increment the freq of the digit we earlier decremented before exploring that path. typical backtracking way

        so once we compute a result that is not equal to 0, we have an answer, and we just need to keep on returning that answer as we go up the recursion stack

        TC: O(9^d) since for each position, we could possibly explore nine paths (1 to 9) in the hashmap, and d is the number of digits, which in worse case is 7 or 8
        SC is constant also

        '''
        digitCounter = {
            1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9
        }

        def backtrack(num, current, count):
            if count == 0:
                for digit, freq in digitCounter.items():
                    if freq != 0 and freq != digit:
                        return 0

                return current if current > num else 0

            result = 0
            for digit in digitCounter:
                # we check that we still have numbers to use and that the number is lesser than or equal to the amount of digits we still need
                # no need picking a 7 when count remains 2, cos we will need 7 digits
                if digitCounter[digit] != 0 and digitCounter[digit] <= count:
                    digitCounter[digit] -= 1
                    result = backtrack(num, current * 10 + digit, count - 1)
                    digitCounter[digit] += 1

                if result != 0:
                    return result

            return result
            

        count = len(str(n))
        result = backtrack(n, 0, count)
        if result == 0:
            result = backtrack(n, 0, count + 1)
        return result
        



class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        '''
        The bruteforcey approach is to check each number after that number and check if it is a balanced number until we get to the first number that is balanced
        and since we know that we would always get to that number we can use the while True and not risk an infinite loop

        TC: O(C - n) where C is the largest possible valid balanced number given the constraints ie 1224444, and n is the input number
        SC: O(1)
        '''
        num = n + 1

        def isBalanced(num):
            count = {}
            for ch in str(num):
                digit = int(ch)
                count[digit] = count.get(digit, 0) + 1

            for digit, freq in count.items():
                if digit != freq:
                    return False

            return True

        while True:
            if isBalanced(num):
                return num
            num += 1


        