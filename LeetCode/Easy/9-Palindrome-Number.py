class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Most optimal way to do this, is to reverse about half of the number and compare with each other, 
        we know that we have gotten to about half when x (the original number) becomes equal to or less than reversedNumber,
        so we keep on reversing till x is no longer greater than reversedNumber

        there is an edgecase tho, for numbers ending with zero, there are never going to be palindromes, since we cannot have leading zeros in
        integers, the only exception is for 0 itself. so we have to explicitly check for that, else we gwt wrong answers for testcases like 12210

        eg for 1221, if we reverse the ending 21, it becomes 12, so that 12 equals 12 in the first half
        this works perfectly for even length numbers, but for odd length numbers eg 585, when we stop reversing, x = 5 and reversedNumber = 58
        so we can ignore that 8 and compare x with the rest of the numbers

        what we return is the two checks, one would trigger if x length is even or odd

        TC: O(log10(N)) because we divide the input by 10 for every iteration
        SC: O(1) Even though revertedNumber can grow as big as half of x, it’s just a single integer variable, 
            not a separate data structure, so the auxiliary space is constant
        '''
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversedNumber = 0

        while x > reversedNumber:
            digit = x % 10
            x = x // 10

            reversedNumber = reversedNumber * 10 + digit

        return x == reversedNumber or x == reversedNumber // 10


        '''
        One way is to actually just reverse the integer itself using modulo and division operators and check if it is the same with the original
        TC: O(N), SC: O(N)
        '''
        if x < 0:
            return False

        num = x
        result = 0
        while num != 0:
            digit = num % 10
            num = num // 10

            result = result * 10 + digit

        return result == x



        '''
        one way is to use two pointers, but without converting to a string, we manipulate the modulus and division operators to get us the digits at the left and right each time
        in order for us to compare.
        A negative number can never be a palindrome because of its negative sign. e.g -121, in reversed it is 121-, so this isn't a palindrome
        
        we use examples to figure out how to get right and left digit, we need a divisor (div) that is based on how big the integer is
        for number like 5, we need 1, for 121, we need 100, for 1221 we need 1000. so we use a while loop and start div from 1, so while our number is greater than or equal to
        div * 10, (the or equal to there handles when our input is a power of 10 itself), we can increase our div to div * 10, that way we get the right divisor

        after comparing, we then need to get rid of the right and left digit, num % div gets rid of the left digit and integer division by 10 gets rid of the right digit,
        then we update our div by dividing it by 100, since two digits just got removed and our number is now smaller

        TC: O(N), where N is the number of digits,
        SC: O(1)  
        '''
        num = x # make copy of the integer so we do not mutate input given (good practice)
        if num < 0:
            return False
        
        div = 1
        while num >= div * 10:
            div = div * 10

        while num != 0:
            right = num % 10
            left = num // div

            if right != left:
                return False

            num = (num % div) // 10
            div = div / 100
        return True


        # Convert to string then run normal palindrome check using two pointers
        num = str(x)
        l, r = 0, len(num) - 1

        while l < r:
            if num[l] != num[r]:
                return False
            l += 1
            r -= 1

        return True
        