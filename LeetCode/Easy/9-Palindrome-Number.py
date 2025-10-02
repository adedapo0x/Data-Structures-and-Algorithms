class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        More optimal way is to use two pointers, but without converting to a string, we manipulate the modulus and division operators to get us the digits at the left and right each time
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
        