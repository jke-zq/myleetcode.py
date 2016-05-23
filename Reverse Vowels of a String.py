class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = "aeiou"
        strs = list(s)
        i, j = 0,len(s) - 1
        while i < j:
            if strs[i].lower() not in vowels:
                i += 1
            elif strs[j].lower() not in vowels:
                j -= 1
            else:
                strs[i], strs[j] = strs[j], strs[i]
                i += 1
                j -= 1
        return "".join(strs)