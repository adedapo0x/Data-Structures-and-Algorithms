class Solution:
    def reverse(self, x: int) -> int:
        '''
        Optimal approach, here the idea is to pop off digits from x one by one from behind and use it to build our answer (res)
        but before we add to res, we have to check and make sure that adding to res doesn't cause res to go out of bounds

        the bounds here is the 32 bit integer constraint, Python doesn't have any built in max size for 32 bit integer, what we have is sys.maxsize which is more of 64 bit size
        so we have to explicitly state maxInt and minInt sizes

        to get the last digit of x, we take the modulus of x by 10 and to get the new x after chopping off the digit, we divide by 10
        but we cannot do this straightforward with % and // because of how Python handles division and mod of negative numbers, it doesn't handle it the way we want
        so we use math.fmod(x, 10) to do our mod % 10 to get the digits, then convert to int, and do normal division, get float, convert to int also to get the new x after last digit is removed

        so before we add to res, we need to check if adding would make res go out of bounds, so we check if what we currently have is already greater or lesser than maxInt/minInt without the last digit,
        or if there are equal, if the last digit that will add to it would not make it go beyond or below our boundary

        we can then change res, to change 29 to 293, we basically multiply by 10, 290 then add 3. so that's what we do

        TC: O(N) where N is the number of digits in x
        SC: O(1)
        
        '''
        original = x
        ans = 0
        maxInt = (2 ** 31) - 1
        minInt = - (2 ** 31)

        while original != 0:
            digit = int(math.fmod(original, 10))
            original = int(original / 10)

            if (ans > maxInt // 10) or (ans == maxInt // 10 and digit > maxInt % 10):
                return 0

            if ans < int(minInt / 10) or (ans == int(minInt / 10) and digit < math.fmod(minInt ,10)):
                return 0

            ans = ans * 10 + digit

        return ans
    

        # lesser lines of code still involves string conversion and reversing as below
        original = x
        x = abs(x)

        x = int(str(x)[::-1])
        if original < 0:
            x *= -1

        if x < -(2 ** 31) or x > 2 ** 31 - 1:
            return 0
        return x
        

        isNegative = False
        strX = str(x)
        reverse = 0
        if x < 0:
            isNegative = True
            strX = strX[1:]
            reverse = int(strX[::-1])
            if reverse > (2 ** 31) -1 or reverse < -(2 ** 31):
                return 0
            return -reverse
        
        else:
            reverse = int(strX[::-1])
            if reverse > (2 ** 31) -1 or reverse < -(2 ** 31):
                return 0
            return reverse



        # reversed = 0
        # isNegative = False
        # if x < 0:
        #     isNegative = True
        #     x *= -1
        # while x > 0:
        #     digit = x % 10
        #     x = x // 10
        #     reversed = (10 * reversed) + digit
        #     if reversed > (2 ** 31) -1 or reversed < -(2 ** 31):
        #         return 0
        # if isNegative: return -reversed
        # return reversed
