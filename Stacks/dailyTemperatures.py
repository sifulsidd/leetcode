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