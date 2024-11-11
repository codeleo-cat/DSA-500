from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_map = Counter(nums)
        for key in nums_map.keys():
            if nums_map[key] == 1:
                return key