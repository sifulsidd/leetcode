# O (klog(n)) time
# O (2k) space, O(k) space

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # first use a hashmap to count the number of items and occurences
        occurences = {}
        for num in nums:
            if num not in occurences:
                occurences[num] = 0
            occurences[num] += 1
        
        # sort the array based on the items values
        items = occurences.items()
        res = []
        counter = 0
        items.sort(key=lambda values: values[1])

        for i in range(len(items) - 1, -1, -1):
            counter += 1
            ans = int(items[i][0])
            res.append(ans)
            if counter == k:
                break
        return res
    
    
    
    
# bucket sort
# uses an array of arrays to find occurences, so no sorting required, then just go through values and add 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # first use a hashmap to count the number of items and occurences
        occurences = {}
        # create an array of length nums, can just append at each iteration below
        track = [[]]
        for num in nums:
            if num not in occurences:
                occurences[num] = 0
            occurences[num] += 1
            track.append([])
        
        # store the occurences of items with the number that's associated
        for key,val in occurences.items():
            track[val].append(key)
        
        res = []
        # loop through the track array, and add integers until the length is equal to result
        for i in range(len(track) - 1, 0, -1):
            for value in track[i]:
                res.append(value)
                if len(res) == k:
                    return res
    
    