class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for token in tokens:
            if token == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 + val1)
            elif token == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif token == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2*val1)
            elif token == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(float(val2)/val1))
            else:
                stack.append(int(token))
        return stack[0]
    
    