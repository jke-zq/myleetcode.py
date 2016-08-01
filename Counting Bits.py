class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        ans = [0, 1]
        count = 2
        while count < num + 1:
            for i in range(len(ans)):
                if count == num + 1:
                    return ans
                else:
                    ans.append(ans[i] + 1)
                    count += 1
        return ans

