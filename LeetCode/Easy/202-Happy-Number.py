class Solution:
    def isHappy(self, n: int) -> bool:

        def getSum(n):
            # takes the last digit and get its square adding it little by little to the total until n has finished
            total = 0
            while n > 0:
                remainder = n % 10
                total += remainder ** 2
                n = n // 10
            return total

        slow = getSum(n)
        fast = getSum(getSum(n))

        # uses Floyd detection algorithm, where we use fast and slow pointers, should the fast pointer ever meet up and equate with the slow pointer, 
        # that means a cycle exists and we want to stop as the loop would keep on running forever. so we keep on looping, until either a cycle appears or
        # the num becomes 1

        # TC is like O(log10n) the tc to compute square is O(log10n) eg 100, we do it 3 times, so its near about O(log10n)

        while slow != fast and fast != 1:
            slow = getSum(slow)
            fast = getSum(getSum(fast))
            
        return fast == 1
    

        '''
        Approach here is to keep on adding as requested by the question. If we find 1, we return True as the number is a happy number
        else, if we come across a number we have previously seen in our set, we return False, as this would lead to a cycle and we keep on checking forever
        '''
        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            total = 0
            for ch in str(n):
                total += int(ch) ** 2
            n = total

        return True if n == 1 else False


        