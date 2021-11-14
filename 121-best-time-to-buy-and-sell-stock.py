class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('Inf')
        max_profit = 0
        
        for i in range(0, len(prices)):
            if min_price >= prices[i]:
                min_price = prices[i]
            else:
                if (prices[i] - min_price >= max_profit):
                    max_profit = prices[i] - min_price
        return max_profit
