class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cherry = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1 , -1):
            if digits[i] + cherry == 10:
                cherry = 1
                digits[i] = 0
            else:
                digits[i] += cherry
                cherry = 0
                break
        if cherry:
            digits.insert(0, 1)
        return digits
        