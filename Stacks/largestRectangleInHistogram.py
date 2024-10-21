class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = [] #pair: (index,height)
        # what we do is initially we set the start to current index
        # afterwards if the top of the stack has a bigger height than current index, we have to find the area of that stack element
        # because its bigger than the current height, we have to take that index and make it the current index, because it is stating our widths work out
        # finally we append the start and the height to the stack
        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append([start, h])
        
        # after the first iteration our stack is still not empty, so we have to go through it 
        # this iteration basically goes to the end of the heights list, so we can use that as the width and subtract is from the given indexes 
        # multiply it by height and all good 
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea