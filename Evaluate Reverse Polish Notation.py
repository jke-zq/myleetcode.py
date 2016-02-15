class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def doOps(v1, v2, ops):
            if ops == '*':
                return v1 * v2
            elif ops == '/':
                return int(v1 * 1.0 / v2)
            elif ops == '+':
                return v1 + v2
            elif ops == '-':
                return v1 - v2
                
        stack = []
        opes = ['+', '-', '*', '/']
        
        for t in tokens:
            if t not in opes:
                stack.append(int(t))
            else:
                v1, v2 = stack.pop(), stack.pop()
                ret = doOps(v2, v1, t)
                stack.append(ret)
        return stack[0]
##using operator