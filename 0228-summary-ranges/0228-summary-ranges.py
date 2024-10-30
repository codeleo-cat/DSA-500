class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = nums[0]

        for i in range(1, len(nums)+1):
            if i==len(nums) or nums[i] - nums[i-1] !=1:
                if start == nums[i-1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i-1]}")
                if i<len(nums):
                    start = nums[i]
        return ranges