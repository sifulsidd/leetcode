class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        # first find the minimum value and maximum value in piles
        minVal, maxVal = 1, max(piles)
        ans = maxVal
        while minVal <= maxVal:
            midVal = (minVal + maxVal) // 2
            time = 0
            for i in piles:
                time += math.ceil(float(i)/midVal)
            if time <= h:
                ans = min(midVal, ans)
                maxVal = midVal - 1
            else:
                minVal = midVal + 1
            
        return ans
            

        