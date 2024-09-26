def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        wordOneAmount = {}

        for letter in s:
            if letter not in wordOneAmount:
                wordOneAmount[letter] = 0
            wordOneAmount[letter] += 1
        
        for letter in t:
            if (letter not in wordOneAmount) or (wordOneAmount[letter] <= 0):
                return False
            wordOneAmount[letter] -= 1
        
        for k,v in wordOneAmount.items():
            if wordOneAmount[k] != 0:
                return False
        return True
    
    
    # essentially we create a dictionary for the first word and keep track of how often we see the letters
    # then our second loop is basically checking if the letters are in the dictionary or if their quantities ever get below 0
    # if either of this happen, we return false
    # finally we loop over items, if the value isn't 0, we return False
    # return true otherwise 