class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftmin = []

        left = float('inf')
        right = 0

        for num in prices:
            if num < left:
                left = num
                leftmin.append(num)
            else:
                leftmin.append(left)

        for i in range(len(prices)-1,-1,-1):
            if prices[i] > right:
                right = prices[i]
            
            leftmin[i] = right - leftmin[i]

        return max(leftmin)                      