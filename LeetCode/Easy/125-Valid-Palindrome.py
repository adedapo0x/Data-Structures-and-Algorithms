class Solution:
    def isPalindrome(self, s: str) -> bool:

        # loops, then uses built in alphanum() method to check string before reversing and checking
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


        # personal first solution, using re module  to check for alphanumeric and using split, join
        # import re
        # arr = re.split('[^a-z0-9]', s.lower()) 
        # newStr = ''.join(arr)
        # return newStr[0::] == newStr[::-1]


        