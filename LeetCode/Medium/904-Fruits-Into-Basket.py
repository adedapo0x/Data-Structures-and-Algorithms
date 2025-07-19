class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
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