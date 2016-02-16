import operator
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ##solution one
        ret = []
        OPS = {'+':operator.add, '-':operator.sub, '*':operator.mul}
        for i in range(len(input)):
            if input[i] in OPS:
                for x in self.diffWaysToCompute(input[:i]):
                    for y in self.diffWaysToCompute(input[i + 1:]):
                        ret.append(OPS[input[i]](x, y))
        if not ret:
            ret = [int(input)]
        return ret