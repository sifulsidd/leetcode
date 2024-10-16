class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # create an array of max and min at each height
        maximumLeft = []
        maximumRight = []
        maxLeft = 0
        maxRight = 0
        for i in height:
            maximumLeft.append(maxLeft)
            maxLeft = max(maxLeft, i)
            maximumRight.append(0)
        for i in range(len(height) - 1, -1, -1):
            maximumRight[i] = maxRight
            maxRight = max(maxRight, height[i])
            
        total = 0
        for h in range(len(height)):
            calc = min(maximumLeft[h], maximumRight[h]) - height[h]
            if calc > 0:
                total += calc
            
        return total

