class Solution:
    def maxProfit(self, prices) -> int:
        """
        type nums: List[int]
        rtype: int
        """
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            current_profit = prices[i] - buy
            if current_profit < 0:
                buy = prices[i]
            elif current_profit > max_profit:
                max_profit = current_profit
        return max_profit

