class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        n = len(prices)
        for right in range(1,n):
            if left != right:
                if prices[left] < prices[right]:
                    profit = prices[right] - prices[left]
                    max_profit = max(max_profit, profit)
                else:
                    left = right
        return max_profit

        