# O(n) time and memory

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


# O(n) time O(1) memory
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        total = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                calc = maxL - height[l]
                maxL = max(maxL, height[l])
            else:
                r -= 1
                calc = maxR - height[r]
                maxR = max(maxR, height[r])
            if calc > 0:
                    total += calc
        return total