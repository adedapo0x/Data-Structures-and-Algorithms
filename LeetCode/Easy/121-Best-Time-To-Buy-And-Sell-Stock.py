class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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