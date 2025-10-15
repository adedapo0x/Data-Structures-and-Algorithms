class Solution:
    def reverse(self, x: int) -> int:

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
