class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # first sort it all 
        nums.sort()
        ans = []
        for i in range(len(nums)): 
            l,r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[r] + nums[l]
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    break
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans         

