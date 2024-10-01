# just skip

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        l,r = 0, 1

        while r < len(prices):
            left = prices[l]
            right = prices[r]
            if right < left:
                l = r
                left = prices[l]
            profit = right - left
            maxProfit = max(profit, maxProfit)
            r += 1
        return maxProfit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        l,r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit