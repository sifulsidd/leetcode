class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # binary search 
        l, r = 0, len(nums) - 1
        ans = nums[r]
        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            
            m = (l + r) // 2
            ans = min(ans, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return ans