class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(temperatures)):
            ans.append(0)
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans
    
    # use a while loop within the for loop, it's still only O(n) time and space, because we only have to go through values once
    class Solution(object):
        def dailyTemperatures(self, temperatures):
            """
            :type temperatures: List[int]
            :rtype: List[int]
            """
            stack = [0]
            ans = [0 for i in temperatures]
            
            for i in range(1, len(temperatures)):  
                while stack and temperatures[i] > temperatures[stack[-1]] :
                    index = stack.pop()
                    ans[index] = i - index
                stack.append(i)
            return ans
