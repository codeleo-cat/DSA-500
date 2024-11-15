class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x_list = [num for num in str(x)]
        # return x_list[:] == x_list[::-1]
        return str(x) == str(x)[::-1]