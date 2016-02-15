import operator
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        exp = []
        i = 0
        while i < len(s):
            if s[i] in ['(',')', '+', '-']:
                exp.append(s[i])
                i += 1
            elif s[i].isdigit():
                ns = ""
                while i < len(s) and s[i].isdigit():
                    ns += s[i]
                    i += 1
                exp.append(int(ns))
            elif s[i] == ' ':
                i += 1
        exp.insert(0, '(')
        exp.append(')')
        stack = []
        ops = {"+": operator.add, "-": operator.sub}
        for op in exp[::-1]:
            if op == ' ':
                continue
            elif op == '(':
                while stack[-2] != ')':
                    v1, optor, v2 = stack.pop(), stack.pop(), stack.pop()
                    stack.append(ops[optor](v1, v2))
                val = stack.pop()
                stack.pop()
                stack.append(val)
            elif type(op) == int:
                stack.append(int(op))
            else:
                stack.append(op)
        return stack[0]