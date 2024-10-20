class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        combined = []
        for i in range(len(position)):
            combined.append([position[i], speed[i]])
        combined.sort()
        
        stack = []
        for i in range(len(combined) - 1, -1, -1):
            pos, speed = combined[i][0], combined[i][1]
            time = (target-pos) / float(speed)
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
            
        return len(stack)
    
    
# non stacks
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        combined = [[position[i], speed[i]] for i in range(len(position))]
        
        total = 0
        curTime = 0
        for p,s in sorted(combined, reverse = True):
            time = (target - p)/float(s)
            if time > curTime:
                total += 1
                curTime = time
        return total