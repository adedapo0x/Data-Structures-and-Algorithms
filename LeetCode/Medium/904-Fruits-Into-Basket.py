class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        Better approach. Here we use the sliding window approach, we keep a slinding window across the members of the element
        and use a dictionary to keep track of elements and the count of them we have seen so far. so once the number of elements in the dict is 
        greater than 2, we want to keep decrementing from the count and shifting our left pointer until the value at our left pointer no longer exists in our
        dictionary, we use a while here because the element could be multiple. e.g [1,1,1,4,5,8], so to get rid of 1 from our window, we will need to use a while
        to decrement count from the dict and increment our left pointer

        TC: O(N)
        SC: O(N)
        '''
        ans = 0
        basket = {}

        l = r = 0
        while l <= r and r < len(fruits):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
                
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            
            ans = max(ans, r - l + 1)

            r += 1

        return ans

        '''
        Bruteforce approach here, we get TLE on Leetcode
        where we start from i and go downwards in the array. we use a set for every i as a starting point, to keep track of elements we have seen, once the 
        number of elements we have come across is greater than 2, no point looking further, we break and try to start from the next i position.
        After every i is done, we compare values together, then at the final end, we return the maxNum

        TC: O(N^2)
        SC: O(N)
        '''
        maxNum = 0
        
        for i in range(len(fruits)):
            total = 0
            basket = set()
            for j in range(i, len(fruits)):
                if fruits[j] not in basket:
                    basket.add(fruits[j])

                if len(basket) <= 2:
                    total += 1
                else:
                    break
            maxNum = max(maxNum, total)
        return maxNum