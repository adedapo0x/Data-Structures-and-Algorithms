class Solution:
    def isPalindrome(self, s: str) -> bool:





        # personal first solution, using re module  to check for alphanumeric and using split, join
        import re
        arr = re.split('[^a-z0-9]', s.lower()) 
        newStr = ''.join(arr)
        return newStr[0::] == newStr[::-1]


        