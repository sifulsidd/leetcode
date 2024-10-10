class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l = 0 
        r = len(height) - 1
        while l < r: 
            h = min(height[l], height[r])
            w = r - l 
            area = h * w 
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea