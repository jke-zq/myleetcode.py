class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        dicts = path.split('/')
        stack = []
        for d in dicts:
            if d == "..":
                if stack:
                    # # raise Exception('invalid')
                    # return "/"
                    stack.pop()
            elif d != "." and d != '':
                stack.append(d)
        ans = '/' + '/'.join(stack)
        return ans