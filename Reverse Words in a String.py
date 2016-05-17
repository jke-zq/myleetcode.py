class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ss = s.split(' ')
        return ' '.join(filter(lambda x: x != '', ss[::-1]))