class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0         
        # use a set 
        s = set(nums)
        for num in nums: 
            longest = 0
            if num - 1 in s:
                continue
            x = num 
            while x in s:
                longest += 1
                x = x + 1
            res = max(longest, res)
        return res
    
    