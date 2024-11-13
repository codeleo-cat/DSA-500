class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10
            if _sum in seen:
                return False
            seen.add(_sum)
            n = _sum
        return True