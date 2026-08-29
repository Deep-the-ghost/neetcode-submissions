class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftmin = []
        rightmax = [0]*len(prices)
        profits = [0]*len(prices)

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
                rightmax[i] = right
            else:
                rightmax[i] = right

            profits[i] = rightmax[i]-leftmin[i]

        return max(profits)                      