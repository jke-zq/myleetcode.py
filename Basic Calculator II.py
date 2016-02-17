import operator
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        OPRS = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.div}
        slist = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] in OPRS:
                slist.append(s[i])
                i += 1
            elif s[i].isdigit():
                nstr = ''
                while i < len(s) and s[i].isdigit():
                    nstr += s[i]
                    i += 1
                slist.append(int(nstr))
        stack = []
        for op in slist[::-1]:
            if op in ['+', '-']:
                while len(stack) > 2 and stack[-2] in ['*', '/']:
                    v1, opr, v2 = stack.pop(), stack.pop(), stack.pop()
                    stack.append(int(OPRS[opr](v1 * 1.0, v2)))
                stack.append(op)
            else:
                stack.append(op)
        while len(stack) > 2:
            v1, opr, v2 = stack.pop(), stack.pop(), stack.pop()
            stack.append(int(OPRS[opr](v1 * 1.0, v2)))
        return stack[0]
##using recursive