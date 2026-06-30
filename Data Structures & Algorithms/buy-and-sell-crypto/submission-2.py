class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max_profit = 0

        for i in range(len(prices)-1):
            current_price = prices[i]

            for j in range(i+1, len(prices)):
                compared_price = prices[j]
                difference = compared_price - current_price
                curr_max_profit = max(difference, curr_max_profit)

        return curr_max_profit