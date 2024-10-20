class MinStack(object):

    def __init__(self):
        # use an array with that has two elements
        self.arr = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.arr) == 0:
            self.arr.append([val,val])
        else:
            currMin = self.arr[-1][1]
            newMin = min(currMin, val)
            self.arr.append([val, newMin])
        

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.arr[-1][1]

# using 2 stacks instead of 1
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            currMin = self.min[-1]
            newMin = min(currMin, val)
            self.min.append(newMin)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
