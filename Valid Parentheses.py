class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {')':'(', ']':'[', '}':'{'}
        queue = []
        for c in s:
            if match.has_key(c):
                if not queue or queue.pop() != match[c]:
                    return False
            else:
                queue.append(c)
        return not queue
            