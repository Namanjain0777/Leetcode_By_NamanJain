class Solution(object):
    def myPow(self, x, n):
        def calc_power(x, n):
            if n == 0:
                return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        current_product = x
        
        while n > 0:
            if n % 2 == 1:  # If n is odd
                result *= current_product
            current_product *= current_product
            n //= 2
        
        return result
