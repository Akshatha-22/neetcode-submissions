class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # you could use positive infinite as well
        min_price = prices[0]

        for i in range(len(prices)):
            # the lowwest price we could have currently
            min_price = min(prices[i], min_price)

            # current profit
            profit = prices[i] - min_price

            # update max profit
            max_profit = max(max_profit, profit)
        
        return max_profit