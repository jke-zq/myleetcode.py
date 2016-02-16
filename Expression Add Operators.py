class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def calculate(s):
            OPRS = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.div}
            slist = s
            # slist = []
            # i = 0
            # while i < len(s):
            #     if s[i] == ' ':
            #         i += 1
            #         continue
            #     elif s[i] in OPRS:
            #         slist.append(s[i])
            #         i += 1
            #     elif s[i].isdigit():
            #         nstr = ''
            #         while i < len(s) and s[i].isdigit():
            #             nstr += s[i]
            #             i += 1
            #         slist.append(int(nstr))
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
        def dfs(num, left, right, exp, exps):
            if left > right:
                exps.append(exp[::])
            else:
                next = left
                while next <= right:
                    if next > left and num[left] == '0':
                        break
                    else:
                        exp.append(int(num[left:next + 1]))
                        for op in ['*', '-', '+']:
                            exp.append(op)
                            dfs(num, next + 1, right, exp, exps)
                            exp.pop()
                        exp.pop()
                    next += 1
        exps = []
        exp = []
        dfs(num, 0, len(num) - 1, exp, exps)
        # print exps
        rets = filter(lambda x: calculate(x) == target, exps)
        return map(lambda x:"".join([str(k) for k in x]), rets)