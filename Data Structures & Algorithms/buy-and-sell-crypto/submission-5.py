class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = float('-inf')
        right = 0


        for i in range(len(prices)-1,-1,-1):
            if prices[i] > right:
                right = prices[i]
            maxprofit = max(maxprofit,right-prices[i])    
        return maxprofit        
