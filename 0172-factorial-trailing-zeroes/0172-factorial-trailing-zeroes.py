class Solution:
    def trailingZeroes(self, n: int) -> int:
        # the_product = 1
        # while n > 0:
        #     the_product *= n
        #     n = n - 1

        # # using list comprehension
        # the_products = [int(num) for num in str(the_product)]
        
        # zeros = 0
        # for n in the_products[::-1]:
        #     if n == 0:
        #         zeros += 1
        #     else:
        #         return zeros
        # return zeros
        zeros = 0
        while n > 0:
            n //= 5
            zeros += n
        return zeros