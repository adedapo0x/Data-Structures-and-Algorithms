class Solution:
    def isPalindrome(self, s: str) -> bool:
        # best solution I think using two pointers and using python built-in isalnum() method
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1 
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True



    # another solution using two pointers, but building our own helper function to check 
    # if character is alphanumeric

    #     l, r = 0, len(s) - 1
    #     while l < r:
    #         while not self.alpha(s[l]) and l < r:
    #             l += 1
    #         while not self.alpha(s[r]) and r > l:
    #             r -= 1 
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l, r = l + 1, r - 1
    #     return True


    # def alpha(self, s):
    #     return ((ord("A") <= ord(s) <= ord("Z"))
    #         or (ord("a") <= ord(s) <= ord("z"))
    #         or (ord("0") <= ord(s) <= ord("9")))






        # loops, then uses built in alphanum() method to check string before reversing and checking
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]


        # personal first solution, using re module  to check for alphanumeric and using split, join
        # import re
        # arr = re.split('[^a-z0-9]', s.lower()) 
        # newStr = ''.join(arr)
        # return newStr[0::] == newStr[::-1]


        