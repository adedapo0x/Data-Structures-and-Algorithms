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


        