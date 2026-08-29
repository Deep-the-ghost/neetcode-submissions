class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        left = prices.index(min(prices))
        right = 0


        for i in range(len(prices)-1,-1,-1):
            if prices[i] > right:
                right = prices[i]
            
            if (right - prices[left]) > maxprofit:
                maxprofit = right - prices[left]
            if i == left: break    

        return maxprofit                