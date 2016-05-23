class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        values = preorder.split(',')
        stack = []
        for v in values:
            if v != '#':
                stack.append(v)
            else:
                while stack and stack[-1] == '#':
                    stack.pop()
                    if not stack or stack[-1] == '#':
                        return False
                    stack.pop()
                stack.append(v)
        return stack == ['#']
                    

## better Solution
#### 1.split_iter
#### 2.'#' if one more than not '#'
        def split_iter(s, tok):
            start = 0
            for i in xrange(len(s)):
                if s[i] == tok:
                    yield s[start:i]
                    start = i + 1
            yield s[start:]

        if not preorder:
            return False

        depth, cnt = 0, preorder.count(',') + 1
        for tok in split_iter(preorder, ','):
            cnt -= 1
            if tok == "#":
                depth -= 1;
                if depth < 0:
                    break
            else:
                depth += 1
        return cnt == 0 and depth == -1