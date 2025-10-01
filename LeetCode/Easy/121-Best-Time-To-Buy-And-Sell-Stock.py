class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # A more straightforward implementation to me
        profit = 0
        l = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[l]:
                profit = max(profit, prices[i] - prices[l])
            else:
                l = i
        return profit



        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit


        # l, r = 0, 1
        # profit = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         diff = prices[r] - prices[l]
        #         profit = max(profit, diff)
        #     else:
        #         l = r
        #     r += 1            
        # return profit