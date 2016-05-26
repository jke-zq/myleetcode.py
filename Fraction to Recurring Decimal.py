class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        def helper(numerator, denominator):
            if numerator * denominator < 0:
                return '-' + helper(abs(numerator), abs(denominator))
            numerator = abs(numerator)
            denominator = abs(denominator)
            if numerator > denominator:
                left = numerator % denominator
                lessPart = '0'
                if left > 0:
                    lessPart = helper(left, denominator)
                return str(numerator / denominator) + lessPart[1:]
            
            leftV = []
            result = []
            left = numerator
            while left > 0:
                while left < denominator:
                    leftV.append(left)
                    result.append(0)
                    left *= 10
                leftV.append(left)
                result.append(left / denominator)
                left = left % denominator
                left *= 10
                if left in leftV:
                    break
                
            if left == 0:
                return '0.' + ''.join([str(v) for v in result[1:]])
            else:
                index = leftV.index(left)
                ans = '0.' + ''.join([str(v) for v in result[1:index]])
                ans += '(' + ''.join([str(v) for v in result[index:]]) + ')'
                return ans
                
                
                    
        if denominator == 0:
            return float('inf')
        if numerator == 0:
            return '0'
        return helper(numerator, denominator)

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        dvd = abs(numerator)
        dvs = abs(denominator)
        integer = str(dvd / dvs)
        dvd = dvd % dvs
        
        
        if dvd > 0:
            integer += '.'
        
        idx = 0
        hashV = {}
        decimal = ''
        while dvd:
            if dvd in hashV:
                decimal = decimal[:hashV[dvd]] + '(' + decimal[hashV[dvd]:] + ')'
                break
            
            hashV[dvd] = idx
            idx += 1
            dvd *= 10
            decimal += str(dvd / dvs)
            dvd = dvd % dvs

        if numerator * denominator < 0:
            return '-' + integer + decimal
        else:
            return integer + decimal
            
            

            