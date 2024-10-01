# just draw out the stack and the way itll work
# not too shabby once thought out

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapped = {"(": ")", 
                  "{":"}", 
                  "[":"]"}

        for ch in s:
            if ch not in mapped:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if mapped[popped] != ch:
                    return False
            else:
                stack.append(ch)
                
        return len(stack) == 0
    
            
        