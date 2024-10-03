class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # first use a hashmap 
        dictionary = {}

        # loop over each element 
        for word in strs:
            # dont use a total amount, use an array of length 26
            total = [0] * 26
            for ch in word:
                # constantly update it based on how many characters are found in the array 
                total[ord(ch) - ord('a')] += 1
            # tuples are immutable(can't be changed), so convert array to this and add it as the key of dictionary
            check = tuple(total)
            if check not in dictionary:
                dictionary[check] = []
            dictionary[check].append(word)
        
        return dictionary.values()