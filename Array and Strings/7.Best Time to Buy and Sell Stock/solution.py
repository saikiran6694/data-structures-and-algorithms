class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        minSoFar = prices[0]
        for i in range(len(prices)):
            minSoFar = min(minSoFar, prices[i])
            profit = prices[i] - minSoFar
            maxSoFar = max(maxSoFar, profit)

        return maxSoFar