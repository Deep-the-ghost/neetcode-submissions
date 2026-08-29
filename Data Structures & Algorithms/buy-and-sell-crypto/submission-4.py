class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = float('-inf')
        right = 0


        for i in range(len(prices)):
            right = max(prices[i:])  
            if maxprofit < (right -prices[i]):
                maxprofit = right - prices[i]
        return maxprofit        
