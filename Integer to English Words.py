class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def treeDigits(num):
            ret = []
            if num / 100:
                ret.append(lookup[num / 100])
                ret.append("Hundred")
            if num % 100:
                ret.append(twoDigits(num % 100))
            return " ".join(ret)
        def twoDigits(num):
            if num in lookup:
                return lookup[num]
            else:
                return lookup[num - num % 10] + " " + lookup[num % 10]
                
        lookup = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        unit = ["", "Thousand", "Million", "Billion"]
        ret = []
        tag = 0
        if num == 0:
            return lookup[num]
        while num:
            left = num % 1000
            word = treeDigits(left)
            if word and tag:
                word += " " + unit[tag]
            if word:
                ret.append(word)
            num /= 1000
            tag += 1
        return " ".join(ret[::-1])