def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # store in a hashmap 
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False
    
    
    # use a hashmanp to keep track of numbers you've seen, if you see it again, return True, otherwise return False