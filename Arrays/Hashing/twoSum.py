def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use a dictionary to store the difference required and the index
        dic = {}

        for i in range(len(nums)):
            lookingFor = target - nums[i]
            if target - nums[i] in dic:
                return [dic[lookingFor], i]
            dic[nums[i]] = i
        return -1
    
    
    # just use a dictionary to store the difference we are looking for 
    # secondly if we find it, we add the dictionary index and the current index and return it 