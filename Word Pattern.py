class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split(' ')
        left_right = {}
        values = set()
        if len(strs) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in left_right:
                if strs[i] in values:
                    return False
                left_right[pattern[i]] = strs[i]
                values.add(strs[i])
            else:
                if left_right[pattern[i]] != strs[i]:
                    return False

        return True
                